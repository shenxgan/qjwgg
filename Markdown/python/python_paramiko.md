#Python 使用 paramiko 模块进行远程调用

[官网](http://www.paramiko.org/)介绍：

> A Python implementation of SSHv2.

###代码示例

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import paramiko


    def ssh_exec_command(hostname, cmd='uname -a', username='root', password='abc', port=22):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, username=username, password=password, port=port, timeout=2, banner_timeout=1)
            stdin, stdout, stderr = ssh.exec_command(cmd, timeout=1)
            output = stdout.read()
            ssh.close()
            return output
        except Exception,e:
            print '%s catch a exception: %s' % (hostname, e)
            return None
            
###高阶使用

可以看看 [Fabric](http://www.fabfile.org/), fabric 封装了 paramiko.