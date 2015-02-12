#linux 虚拟 ip

    :::bash
    #!/bin/bash

    # 版本： v0.2
    # 日期： 2014/12/04
    # 功能： 通过指定起始ip和ip个数，来添加虚拟ip；自动获取当前系统活动网口


    function help
    {
        cat <<EOF
    $0 usage:
        $0 getnetworkport               # 获取当前正在使用的网络端口，一般为 eth0
        $0 removeallip                  # 清除所有的虚拟 ip
        $0 addiprange beginip ipnum     # 添加一个范围内的虚拟 ip，参数为起始 ip 和 ip 个数
        $0 help                         # 输出帮助信息
    EOF
    }

    function valid_ip
    {
        local ip=$1
        echo $ip | grep "^[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}$" > /dev/null
        if [ $? = 1 ]; then
            return 1
        else
            a=`echo $ip | awk -F. '{print $1}'`
            b=`echo $ip | awk -F. '{print $2}'`
            c=`echo $ip | awk -F. '{print $3}'`
            d=`echo $ip | awk -F. '{print $4}'`

            if [ $a -ge 255 -o $a -le 0 -o $b -gt 255 -o $b -lt 0 -o $c -gt 255 -o $c -lt 0 -o $d -gt 255 -o $d -le 0 ]; then
                return 2;
            fi

            #验证是否组播地址
            if [ $a -ge 224 -a $a -le 239 ]; then
                return 3
            fi

            #验证回环
            if [ $a -eq 127 ]; then
                return 4
            fi
        fi
        return 0
    }

    function get_network_port
    {
        for port in `ifconfig | grep eth | awk -F ' ' '{print $1}'`
        do
            echo $port
            return 0
        done

        return 1
    }

    function remove_all_ip
    {
        echo "service network restart..."
        /etc/init.d/network restart
    }

    function add_ip_range
    {
        local begin_ip=$1
        local ip_count=$2

        echo $ip_count | grep "^[0-9]*$" >/dev/null

        if [ $? -ne 0 ]; then
            echo "ip 个数要为整数！"
            return 1
        elif [ $ip_count -le 0 ]; then
            echo "ip 个数要大于0！"
            return 2
        fi

        valid_ip $begin_ip
        if [ $? -ne 0 ]; then
            echo "请输入合法的起始 ip！"
            return 3
        fi

        local begin=`echo $begin_ip | awk -F '.' '{print $4}'`
        local end=$(($begin+$ip_count))

        if [ $end -ge 255 ]; then
            echo "ip 个数太大！"
            return 4
        fi

        network_port=`get_network_port`
        network_segment=`echo $begin_ip | awk -F '.' '{print $1"."$2"."$3"."}'`

        while [ $begin -lt $end ]; do
            echo "ifconfig $network_port:$begin $network_segment$begin"
            ifconfig $network_port:$begin $network_segment$begin
            ((begin++));
        done;
    }


    action="$1"

    case "$action" in
        getnetworkport)
            get_network_port
            exit $?
            ;;
        removeallip)
            remove_all_ip
            exit $?
            ;;
        addiprange)
            if [ $# -ne 3 ];then
                echo "请输入指定的参数个数！"
                help
                exit 0
            fi
            shift
            add_ip_range $@
            exit $?
            ;;
        *)
            help
            exit -1
            ;;
    esac

