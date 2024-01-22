#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os
import logging


# 内存监控
def memory_stat():
    mem = {}
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2:
            continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var)
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    # 记录内存使用率 已使用 总内存和缓存大小
    res = {}
    res['percent'] = int(round(mem['MemUsed'] / mem['MemTotal'] * 100))
    res['used'] = round(mem['MemUsed'] / (1024 * 1024), 2)
    res['MemTotal'] = round(mem['MemTotal'] / (1024 * 1024), 2)
    res['Buffers'] = round(mem['Buffers'] / (1024 * 1024), 2)
    '''
    print('{0}内存使用情况{0}'.format('-'*6))
    print('内存使用率： {}%'.format(res['percent']))
    print('已使用内存： {}G'.format(res['used']))
    print('总内存： {}G'.format(res['MemTotal']))
    print('缓存大小： {}G'.format(res['Buffers']))
    '''
    return res


# CPU负载监控
def cpu_load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=float(con[0])
    loadavg['lavg_5']=float(con[1])
    loadavg['lavg_15']=float(con[2])
    loadavg['nr']=con[3]

    process_list = loadavg['nr'].split('/')
    loadavg['running_process'] = int(process_list[0])
    loadavg['total_process'] = int(process_list[1])
    loadavg['last_pid']=con[4]
    '''
    print('{0}CPU使用情况{0}'.format('-'*6))
    print('1分钟内cpu的平均负载: {}'.format(loadavg['lavg_1']))
    print('5分钟内cpu的平均负载: {}'.format(loadavg['lavg_5']))
    print('15分钟内cpu的平均负载: {}'.format(loadavg['lavg_15']))
    #print(': {}'.format(loadavg['nr']))
    print('正在运行的进程数: {}'.format(loadavg['running_process']))
    print('总进程数: {}'.format(loadavg['total_process']))
    print('最近活跃的进程ID: {}'.format(loadavg['last_pid']))
    '''
    return loadavg


# 磁盘空间监控
def disk_stat(dir):
    hd               = {}
    disk             = os.statvfs(dir) # 指定了查看根目录的磁盘情况
    hd['available']  = float(disk.f_bsize * disk.f_bavail)
    hd['capacity']   = float(disk.f_bsize * disk.f_blocks)
    hd['used']       = float((disk.f_blocks - disk.f_bfree) * disk.f_frsize)
    res              = {}
    res['used']      = round(hd['used'] / (1024 * 1024 * 1024), 2)
    res['capacity']  = round(hd['capacity'] / (1024 * 1024 * 1024), 2)
    res['available'] = res['capacity'] - res['used']
    res['percent']   = int(round(float(res['used']) / res['capacity'] * 100))
    '''
    print("{0}磁盘使用情况{0}".format('-'*6))
    print('使用的磁盘空间量: {}G'.format(res['used']))
    print('可使用的磁盘空间量: {}G'.format(res['capacity']))
    print('剩余可用的磁盘空间量: {}G'.format(res['available']))
    print('已使用的磁盘空间量占比: {}%'.format(res['percent']))
    '''
    return res


# 自己根据实际流程情况考虑采用哪些指标限制流程的启动
def sometime_res(config_d):
    os.system("date")
    cpu_dict = cpu_load_stat()
    mem_dict = memory_stat()
    disk_dict = disk_stat(config_d['data_analysis_dir'])

    run_stat = 0 # 判断启动流程的状态
    # 根目录下小于100G的空间，或者剩余空间小于20%
    if (disk_dict["available"] < config_d['disk_limit']) or (disk_dict['percent'] > config_d['disk_limit_percent']):
        logging.warning('根目录下空间过少！')
    elif mem_dict['percent'] > config_d['ram_limit_percent']:
        logging.warning('内存占用过高！')
    elif cpu_dict['lavg_15'] > config_d['cpu_load_limit_percent']:
        logging.warning('15分钟内cpu负载过高！')
    else:
        run_stat = 1
        logging.info('服务器资源满足分析需求')
    return run_stat


# 默认每隔60秒，调用各监控函数
def watch_res(inc=60):
    while True:
        sometime_res()
        time.sleep(inc)


def main():
    # watch_res(300)
    sometime_res()


if __name__ == '__main__':
    main()

