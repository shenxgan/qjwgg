#net-snmp 扩展自定义 mib 库

在根据自定义的 MIB 文件生成 .c 和 .h 文件之后，将其扩展到 snmpd 中有两种方法：**静态集成**和**动态加载**

####1. 静态集成
个人觉得这种方法比较简单，优点是省事，缺点是耗时长（每次修改都需要重新编译 net-snmp）

方法：将 自定义 MIB 库所生成的 .c 和 .h 文件添加到 .../agent/mibgroup 下面。建议是在 /agent/mibgroup 目录下新建一个文件夹，将所有的 .c 和 .h 文件放在其中。然后重新 ./configure; make; make install

依次为：

    ./configure --with-mib-modules="yourdir/xxx1Table yourdir/xxx2Table"
    # yourdir 为在 /agent/mibgroup 目录下新建的文件夹，xxxxTable为生成的 .c 和 .h 文件
    
    make; make install

####2. 动态加载
动态加载，即为使用动态链接库的方法。

方法：首先正常编译 net-snmp （即直接 ./configure; make; make install），然后自己手动书写 Makefile 将所有生成的 .c 和 .h 文件编译成一个 .so 文件。将此 .so 文件放在一个路径下，并在 snmpd.conf 文件中指定其路径

* 在编译 Makefile 文件的时候，除了指定 -fPIC -shared 参数外，还需要指定 net-snmp 头文件的路径，如

        gcc xxx1Table.c xxx2Table.c -fPIC -shared -o libtestapi.so -I/usr/local/net-snmp/include/

* 在 snmpd.conf 文件中指定 .so 文件路径格式如下：

        dlmod xxx1Table .../libtestapi.so
        dlmod xxx1Table .../libtestapi.so
