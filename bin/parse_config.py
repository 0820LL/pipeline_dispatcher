#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import os
import argparse
from bin.basic_functions import get_pipeline_name, run_cmd


def invoke_pipeline(pipeline_config:str, config_d:dict) -> None:
    analysis_dir = os.path.dirname(pipeline_config)
    pipeline_name = get_pipeline_name(pipeline_config)
    if pipeline_name.strip().lower() == "wes":
        wes_cmd = 'bash {0} {1}'.format(config_d['wes'], pipeline_config)
        logging.info(wes_cmd)
        run_cmd(wes_cmd, analysis_dir)
    elif pipeline_name.strip().lower() == "panel":
        panel_cmd = "bash {0} {1}".format(config_d["panel"], pipeline_config)
        logging.info(panel_cmd)
        run_cmd(panel_cmd, analysis_dir)
    elif pipeline_name.strip().lower() == "wgs":
        wgs_cmd = "bash {0}/run_WGS.sh {1}".format(config_d["wgs"], pipeline_config)
        logging.info(wgs_cmd)
        run_cmd(wgs_cmd, analysis_dir)
    elif pipeline_name.strip().lower() == "rnaseq":
        rnaseq_cmd = "bash {0}/run_mRNA_pipeline.sh {1}".format(config_d["rnaseq"], pipeline_config)
        logging.info(rnaseq_cmd)
        run_cmd(rnaseq_cmd, analysis_dir)
    else:
        with open('{}/Fail.log'.format(analysis_dir), 'w') as fail_f:
            fail_f.write("pipeline name is wrong: {}\n".format(pipeline_name))
        logging.error("pipeline name is wrong: {}\n".format(pipeline_name))

def main():
    parser = argparse.ArgumentParser(description='输入绝对路径的配置文件config.json')
    parser.add_argument('-i', '--input', required=True, help='input file')
    args = parser.parse_args()
    input_config = args.input
    invoke_pipeline(input_config)


if __name__ == '__main__':
    main()
