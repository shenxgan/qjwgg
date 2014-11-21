#ip定位

>系统环境：python2.6.6  
>ip定位API：淘宝IP地址库

我是在写webpy实现留言板的时候想：我能获取用户的ip地址，那么应该也可以通过ip地址获取其地理位置吧。后来就搜索了一下，采用的是[淘宝IP地址库](http://ip.taobao.com/instructions.php)。试验了一下，淘宝这个地址库比较详细，速度也还可以。就采用它了。

使用的关键技术就是`urllib2`这个库，其中核心的函数`ip2addr`，源码如下：

    def ip2addr(ip):
        addr = {}
        addr['country'] =  ''
        addr['region'] =  ''
        addr['city'] = ''
        try:
            url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' %(ip)
            print url
            data = urllib2.urlopen(url)
            addr_json = data.read()
            addr_dict = json.loads(addr_json) ##将json数据格式转换为dict数据格式
            if addr_dict['code'] == 0:
                addr['country'] =  addr_dict['data']['country']
                addr['region'] =  addr_dict['data']['region']
                addr['city'] =  addr_dict['data']['city']
        except Exception, e:
            print e
        finally:
            return addr

很简单，是吧。我只是挑出了国家、省、市三个地址（国外的ip解析后大部分只有国家，其它信息一般为空）。

到此，此函数应该就可以满足你的大部分需求了。但当我进行测试的时候，我发现与我想象中的差距：  

**没有想象中的速度！！！**

这个速度有时候很快（<1s），但我测试的时候也有很大一部分的时间是超过10s的，这个根本就不能容忍！  
因为我是要使用在评论中的，试想一下，当我发表一个评论后，需要等待10几秒才能评论成功，那是怎样的煎熬。

**想到了一个方法：**在urllib2.urlopen的时候加上timeout  
即`urllib2.urlopen(url, timeout=1)`，怀着胜利的心情将修改后的代码运行了一遍。咦，咋五六秒了还没有执行完。后来又连续试了几次，问题依旧。  
后来[搜索](http://www.douban.com/group/topic/46518080/)了一下，发现应该是服务器返回[CHUNKED编码](http://zh.wikipedia.org/zh/%E5%88%86%E5%9D%97%E4%BC%A0%E8%BE%93%E7%BC%96%E7%A0%81)的问题。对于这个，我表示无能为力~

**第二个方法：**抓取淘宝IP地址库来生成自己的IP地址库  
这个方法原理很简单：就是使用多线程，遍历所有的ip去调用淘宝的那个API，将获取的信息存入自己的数据库即可。我感觉太麻烦，遂放弃

**最终使用的方法：**使用线程来执行ip2addr  
这是我在我的评论中使用的方法，即有人发表了一条评论时，开启线程去执行`ip2addr`，当执行完后对数据库进行更新即可。更新时根据ip地址对应唯一物理地址的原则进行更新（webpy获取客户端ip地址：[web.ctx.ip](http://webpy.org/cookbook/ctx.zh-cn)）。

    class ip2address(threading.Thread):
        def __init__(self, ip):
            threading.Thread.__init__(self)
            self.ip = ip
            self.count = 0
            self.setDaemon(True)
            self.start()
    
        def run(self):
            while True:
                self.count += 1
                usrip = self.ip

                addr = ip2addr(self.ip)
                if addr['country'] != '': ##查询到了结果
                    usraddr = addr['country']+addr['region']+addr['city']
                    sql = "update comment set usraddr='%s' where usrip='%s'" %(usraddr, usrip)
                    dbhandler.execute(sql)
                    break
                if self.count >= 5: ##限制最多去查询5次
                    break
    
        def stop(self):
            pass
    
查询到了就去更新数据库，没有则进行循环，最多去获取5次。五次之后不管有木有都直接退出。  
之前想着在调用`ip2addr`前先从数据库去尝试获取的，这样也比较快。但考虑到最好不要操作数据库和说不定以后ip对应的地址发生变化了呢，所以也就没有去从数据库获取了。  

至此，**python+淘宝IP地址库实现的ip定位**记录完毕~

