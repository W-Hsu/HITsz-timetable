*iOS的HIT助手*！

该项目目前还在努力开发之中。

自动爬取由`jw.hitsz.edu.cn`导出的Excel课表文件，并生成**iCal**\(iCalendar, a.k.a. Webcal
[Wiki](https://en.wikipedia.org/wiki/ICalendar)
[百度百科](https://baike.baidu.com/item/iCal)\)格式的日历信息。

虽然iCalendar格式由Apple首先发布，但是该格式目前已经成为事实上的标准。Microsoft Outlook、Google Calendar等带有
日历功能的软件或服务均支持iCal格式的日历信息。

目标：

* 参数解析：命令行和配置文件两种方式
* 可选输出目标：stdout与本地ics文件
    * 向stdout输出时，可以部署在支持**CGI**\(通用网关接口 
    [Wiki](https://en.wikipedia.org/wiki/Common_Gateway_Interface)
    [百度百科](https://baike.baidu.com/item/CGI/607810?fr=aladdin)\)的服务器上
