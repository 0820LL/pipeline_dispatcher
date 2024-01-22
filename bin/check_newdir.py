#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
from bin.watch_server import sometime_res
import os

def check_newdir(input_dir):
    newdir = ''
    for dir_list in os.listdir(input_dir):
        path = os.path.join(input_dir, dir_list)
        if os.path.isdir(path):
            sub_lists = os.listdir(path)
            num_f = len(sub_lists)
            if num_f == 1:
                sub_path = os.path.join(path, sub_lists[0])
                if os.path.isfile(sub_path) and (sub_lists[0] == 'config.json'):
                    newdir = path
                    logging.info(path)
            elif num_f == 2:
                if ('sample-metadata.txt' in sub_lists) and ('config.json' in sub_lists):
                    newdir = path
                    logging.info(path)
                elif ('par.xml' in sub_lists) and ('config.json' in sub_lists):
                    newdir = path
                    logging.info(path)
            else:
                if ('perseus.json' in sub_lists) and ('startper.txt' not in sub_lists):
                    newdir = path
                    logging.info(path)
    return newdir


def run_pipe(path):
    run_stat = 0
    new_dir = check_newdir(path)
    src_tag = sometime_res()
    if src_tag and new_dir != "":
        run_stat = 1
    if run_stat == 1:
        return new_dir


def main():
    import argparse

    parser = argparse.ArgumentParser(description='判断目录中是否有新目录生成，里面是否有config.json文件')
    parser.add_argument('-i', '--input', required=True, help='分析目录路径')
    args = parser.parse_args()
    input_dir = args.input
    new_dir = run_pipe(input_dir)
    #print(new_dir)
#    with open("new_dir_list.txt", "w") as out:
#        out.write(new_dir)


if __name__ == '__main__':
    main()