20240122
==== 说明 ====
这些脚本是用来：
1.监控指定目录下是否出现新的待分析的目录
2.判断服务器的资源（CPU、内存等）是否满足分析需求
3.根据config.json中的内容判断启动相应的生信分析流程

==== 使用方法 ====
所有的配置参数在dispatcher_config.json文件中
在crontab服务器配置周期性执行命令
crontab -e
*/1 * * * * /usr/bin/python3 /data_5t/lilin/products/pipeline_dispatcher/pipeline_dispatcher.py
