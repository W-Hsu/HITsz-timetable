# iOS的HIT助手！

该项目目前正在维护+上新之中。

![screenshot](https://gitee.com/sulphuricacid/image-base/raw/master/2021/HITsz-timetable/IMG_1968.jpg)

截图：至暗时刻

自动爬取由`jw.hitsz.edu.cn`导出的Excel课表文件和考试信息，并生成**iCal**\(iCalendar, a.k.a. Webcal [Wiki](https://en.wikipedia.org/wiki/ICalendar) [百度百科](https://baike.baidu.com/item/iCal)\)格式的日历信息。

虽然iCalendar格式由Apple首先发布，但是该格式目前已经成为事实上的标准。Microsoft Outlook、Google Calendar等带有日历功能的软件或服务均支持iCal格式的日历信息。

## Changelog

### v0.2-beta

* 新增：自动从教务系统爬取校历，无需手动输入第一周星期一的日期！

* 新增：可以生成考试信息啦！

### v0.1-alpha

* 基本功能：生成本学期所有课的课表。只需要输入本学期第一周第一个星期一的日期！

* 可以选择输出到`stdout`或者是指定文件。

## 玩法

* 可以用这个工具生成ics，同步到iOS设备上。方法如下：

  1. 运行本工具。详细命令行参数可以参见[CLI参数说明](#CLI参数说明)

    * 方法1：下载打包好的工具（可以在侧面release中找到）。然后执行`timetable.exe -u <你的学号> -f D:/new.ics`，在D盘根目录下生成`new.ics`文件。

    * 方法2：克隆本仓库，进入克隆好的项目，然后执行`python main.py -u <你的学号> -f D:/new.ics`，效果一样。只是需要安装[依赖](#第三方库依赖)，执行`pip install <需要的库>`即可
  
  2. 将生成的ics文件导入苹果设备
  
    * 方法1：借助Microsoft Outlook、Apple Calendar（如果有一台mac）或Google Calendar（如果可以）进行云同步。
    
    * 方法2：发一封邮件到自己的邮箱，把ics文件作为附件。然后在手机上**用Safari浏览器登录邮箱**，下载附件，点击**全部加入**即可。

* 也可以部署到有**CGI**功能的服务器上。
  
  * **CGI**是**通用网关接口**的英文简称，它可以扩充Web服务器的功能，是一个古老而有效的工具。Apache httpd支持这项功能。
  
  * 此处我们可以利用Python+CGI来提供iCalendar服务。这样的好处是**可以随时更新，不用担心哪天忽然多出一节课没显示**
  
  * 入口文件可以像下面这么写（未验证）。然后就可以通过URL：`webcal://Server-Address/CGI-Program-Path`来订阅日历了。
    
    ```python
    #! C:/Python/Python39/python.exe
    # coding=utf-8
    
    import os
    import subprocess
    import sys, codecs
    
    # 这里是防止Python+CGI出现中文乱码现象
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    
    # 回应头，声明提供iCalendar协议的服务
    print("content-type: text/calendar\n")
    
    # 调起timetable，从标准输出取得webcal payload
    retval, output = subprocess.getstatusoutput("C:/.../timetable.exe -u 123456789 -p ******** --stdout")
    if retval==0:
      for i in output.split('\n'):
          print(i)
    ```

## CLI参数说明

* 必需参数：

  * `-u [Username]`     指定用户名

  * **例子**：我的学号是123456789，想要获取当前学期的课表，命令行参数就设置为：`-u 123456789`

* 可选参数：
  
  * `--year [Year]`     指定学期开始的年份
  
  * `--sem [Semester]`  指定学期（可选项`autumn, fall, spring, summer`，秋秋春夏）
  
  * `-p [Password]`     指定密码。如果不想在shell中留下痕迹可以不填，在运行时会要求输入。
  
  * `-f [FilePath]`     指定输出ics文件的路径
  
  * `--stdout`          将ics文件内容写到标准输出，优先级比`-f`选项高。就是说，指定`--stdout`之后，`-f`就没用了。
  
  * **例子**：我的学号是123456789，密码是__9876543，想要获取2021年春季学期学期的课表，并输出到`D`盘下的
    `123.ics`文件中，命令行参数就设置为：
    `-u 123456789 -p __9876543 --year 2021 --sem spring -f D:/123.ics`

## 第三方库依赖·致谢（通过脚本源码运行时需要用pip安装）

* `click`
* `requests`
* `bs4`
* `openpyxl`
* `icalendar`
* `pyinstaller`（打包用）

*声明：作者还在努力修bug，所以生成的信息可能会不准确。*

*考试之前，别忘了查一下jw系统（狗头*
