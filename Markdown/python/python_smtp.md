#Python发送邮件

>系统环境：Python2.6.6  
>Python库：smtplib

##源代码如下：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    
    import smtplib
    
    TIMEOUT = 10
    
    def sendmail():
    
        sender = '12345678@qq.com'              ##发件人邮箱地址
        passwd = '******'                       ##邮箱密码
        smtphost = 'smtp.qq.com'                ##smtp服务器
        smtpport = 25                           ##smtp端口号
        receivers = ['87654321@qq.com','','']   ##收件人，可指定多个收件人
    
        msg = u'这是测试邮件。'.encode('gb2312')
        message = """From: %s
    To: %s
    Subject: [Python]SMTP e-mail test
    
    %s
    This is the test e-mail.
    
    """%(sender, ';'.join(receivers), msg)
    
        try:
            smtp = smtplib.SMTP(host=smtphost, port=int(smtpport), local_hostname=None, timeout=TIMEOUT)
            smtp.login(sender, passwd)
            smtp.sendmail(sender, receivers, message)
            print "Successfully sent email"
            smtp.quit()
        except Exception ,e:
            print "ERROR: failed sent email"
            print e
    
    if __name__ == '__main__':
        sendmail()


##特别注意：
请特别注意邮件发送内容的编码问题，国内的大部分邮箱的编码默认为gb2312，所以需要进行编码转换。  

##参考：

下述是我整理的一点资料

    :::text
    GB2312字符集
    作用：国家简体中文字符集，兼容ASCII。
    位数：使用2个字节表示，能表示7445个符号，包括6763个汉字，几乎覆盖所有高频率汉字。
    
    GBK字符集
    作用：它是GB2312的扩展，加入对繁体字的支持，兼容GB2312。
    位数：使用2个字节表示，可表示21886个字符。
    
    简体中文 GB2312
    繁体中文 BIG5
    简繁中文 GBK

编码相关：[http://www.cnblogs.com/itech/archive/2011/03/28/1997212.html](http://www.cnblogs.com/itech/archive/2011/03/28/1997212.html)

##结论建议：

在书写在代码中发送邮件时，若邮件正文中包含中文时，需要对中文进行编码  
或编码为gb2312（简体），或编码为gbk（简体+繁体）
