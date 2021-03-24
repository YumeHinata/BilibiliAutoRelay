# BilibiliAutoRelay(bilibili自动转发)

**为确保使用的流畅请确保阅读完以下内容**

## 需要使用的库与软件：

#### python

[Python下载](https://www.python.org/downloads/release)

#### pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

#### selenium

```
pip install selenium
```

#### chrome、chromedriver

[Chrome下载](https://www.google.cn/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#)、[ChromeDriver下载](http://npm.taobao.org/mirrors/chromedriver/)

#### request

```
pip install request
```

**请确保已安装上述软件与库!!!**

## 使用说明：

首次运行请打开“**请在50s内输入账号密码获取cookie.py**”

输入账号密码完成登录，脚本会在50秒后获取cookie并自动关闭，请不要提前关闭。（获取到的cookie会保存在cookies.txt下）

运行“**main_cookie登录_无窗口.py**”

首次运行会生成info.txt（无特殊情况）请不要删除，info.txt会记录已转发的地址以及转发的时间

## 一言Api：

此插件默认启用了一言Api如需更改参数或更换Api请在脚本中修改。

默认ApiUrl：https://v1.hitokoto.cn/?c=a&c=f&c=k&encode=text

一言官方：https://hitokoto.cn/

## 其他：

此脚本在Windows环境下开发只能保证在windows环境下正常使用。

在运行“**main_cookie登录_无窗口.py**”前，可以先运行“**main_cookie登录.py**”，找到适合你服务器的刷新时间。

## 参考信息：

CSDN：[《python+selenium 浏览器无界面模式运行》](https://blog.csdn.net/u011280778/article/details/104283409)——「1学习者1」

CSDN：[《selenium 自动化 携带cookies模拟登陆哔哩哔哩并发送弹幕和评论（解决多窗口切换、规避检测、评论无法输入等问题）》](https://blog.csdn.net/m0_50944918/article/details/112148216)——「乎你」
