#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import sys
import os
from bin.basic_functions import read_json
from bin.check_newdir import check_newdir
from bin.watch_server import sometime_res
from bin.parse_config import invoke_pipeline 

def dispatcher(config_d: dict):
    # check whether there is a new directory generated
    new_dir = check_newdir(config_d['data_analysis_dir'])
    if new_dir:
        src_stat = sometime_res(config_d)
        if src_stat:
            analysis_dir = new_dir
            os.chdir(analysis_dir)
            pipeline_config = '{}/config.json'.format(analysis_dir)
            logging.info(pipeline_config)
            invoke_pipeline(pipeline_config, config_d)
        else:
            logging.warning("系统资源不满足，无法启动分析流程")
            sys.exit()
    else:
        logging.info("{}中没有满足条件的、需要分析的目录".format(analysis_dir))
        sys.exit()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists("{0}/configuration.json".format(script_dir)):
        config_file = "{0}/configuration.json".format(script_dir)
    elif os.path.exists("{0}/../configuration.json".format(script_dir)):
        config_file = "{0}/../configuration.json".format(script_dir)
    else:
        exit("the configuration.json not exist")
    config_d = read_json(config_file)
    log_file = config_d['log_file']
    logging.basicConfig(filename='{}'.format(log_file),level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    dispatcher(config_d)


if __name__ == '__main__':
    main()
