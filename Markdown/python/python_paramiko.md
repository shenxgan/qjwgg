#Python 使用 paramiko 模块进行远程调用

[官网](http://www.paramiko.org/)介绍：

> A Python implementation of SSHv2.

###代码示例

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import paramiko
    import logging

    logging.getLogger("paramiko").setLevel(logging.WARNING)  # 设置其 logging 等级

    def ssh_exec_command(hostname, cmd='uname -a', username='root', password='abc', port=22):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, username=username, password=password, port=port, timeout=2)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            ret = stdout.channel.recv_exit_status()  # 获取执行结果（远程脚本 return 的值）
            output = stdout.read()
            ssh.close()
            return ret,output
        except Exception,e:
            print '%s catch a exception: %s' % (hostname, e)
            return None


    if __name__ == '__main__':
        hostname = '172.10.2.225'
        cmd = 'uname -a'
        ret,output = ssh_exec_command(hostname, cmd)
        print output


###高阶使用

可以看看 [Fabric](http://www.fabfile.org/), fabric 封装了 paramiko.