20240122
==== 说明 ====
这些脚本是用来：
1.监控指定目录下是否出现新的待分析的目录
2.判断服务器的资源（CPU、内存等）是否满足分析需求
3.根据config.json中的内容判断启动相应的生信分析流程

==== 使用方法 ====
所有的配置参数在configuration.json文件中,该文件可以放在脚本dispatcher.py的当前目录也可以其上层目录，其中的参数是所有流程共享的
在crontab服务器配置周期性执行命令
crontab -e
*/1 * * * * /usr/bin/python3 /.../dispatcher.py
