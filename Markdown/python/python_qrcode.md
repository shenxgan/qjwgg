#Python 中使用 qrcode 库生成二维码

##1. 安装使用

在进行安装使用 qrcode 生成二维码的时候，除了安装 qrcode 外，还需要安装 Imaging。因在 qrcode 中会使用到 image 模块

1. 下载安装 qrcode
    * 下载地址 [https://pypi.python.org/pypi/qrcode](https://pypi.python.org/pypi/qrcode)
    * GitHub [https://github.com/lincolnloop/python-qrcode](https://github.com/lincolnloop/python-qrcode)
2. 下载安装 Imaging
    * 下载地址 [http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz](http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz)

下载安装完成后，可在 linux 中敲下如下命令：

    :::bash
    qr "Some text" > test.png

若在当前目录生成了 test.png 的二维码图片，即表示成功。


##2. Python 代码示例

###简单用法：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import qrcode

    img = qrcode.make('just a test.')
    img.save('qr_test.png')    # 保存到指定文件

###高级用法：

    :::python
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    import qrcode

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=1,
    )
    qr.add_data('http://www.qjwgg.com')
    qr.make(fit=True)

    img = qr.make_image()
    img.save('qr_test.png')

参数含义：（[详细内容请点这里](https://github.com/mozillazg/my-blog-file/blob/master/2012/08/python-how-to-generate-qr-code-by-python-qrcode-and-some-real-application.markdown)）

* version：值为1~40的整数，控制二维码的大小（最小值是1，是个12x12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

* error_correction：控制二维码的错误纠正功能。可取值下列4个常量。

    * ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
    * ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
    * ERROR_CORRECT_Q：大约25%或更少的错误能被纠正。
    * ERROR_CORRECT_H：大约30%或更少的错误能被纠正。

* box_size：控制二维码中每个小格子包含的像素数。

* border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）

二维码示例：

![](/static/img/qr_test.png)

###在二维码中间添加图标

在网上搜索到的结果是，带图标的二维码都是通过二维码的容错性来实现的。详情请参考：

[http://dhq.me/python-qr-code-generator](http://dhq.me/python-qr-code-generator)
