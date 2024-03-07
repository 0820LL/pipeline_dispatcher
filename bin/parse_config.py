#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import os
import argparse
from bin.basic_functions import get_pipeline_name, run_cmd, get_ukbTool_name


def invoke_pipeline(pipeline_config:str, config_d:dict) -> None:
    analysis_dir = os.path.dirname(pipeline_config)
    pipeline_name = get_pipeline_name(pipeline_config)
    if pipeline_name.strip().lower() == "wes":
        pipeline_cmd = 'bash {}/{} {}'.format(config_d['project_base_dir'], config_d['wes'], pipeline_config)
    elif pipeline_name.strip().lower() == "panel":
        pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["panel"], pipeline_config)
    elif pipeline_name.strip().lower() == "wgs":
        pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["wgs"], pipeline_config)
    elif pipeline_name.strip().lower() == "rnaseq":
        pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["rnaseq"], pipeline_config)
    elif pipeline_name.strip().lower() == "metabolism":
        pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["metaboigniter"], pipeline_config)
    elif pipeline_name.strip().lower() == 'ukb':
        tool_name = get_ukbTool_name(pipeline_config)
        if tool_name.strip().lower() == 'bwa-men fastq read mapper':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["bwa-men fastq read mapper"], pipeline_config)
        elif tool_name.strip().lower() == 'cnvkit':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["cnvkit"], pipeline_config)
        elif tool_name.strip().lower() == 'deepvariant germline variant caller':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["deepvariant germline variant caller"], pipeline_config)
        elif tool_name.strip().lower() == 'fastqc reads quality control':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["fastqc reads quality control"], pipeline_config)
        elif tool_name.strip().lower() == 'freebayes variant caller':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["freebayes variant caller"], pipeline_config)
        elif tool_name.strip().lower() == 'gatk4 base quality score recalibrator':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["gatk4 base quality score recalibrator"], pipeline_config)
        elif tool_name.strip().lower() == 'gatk4 haplotypecaller':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["gatk4 haplotypecaller"], pipeline_config)
        elif tool_name.strip().lower() == 'rsem calculate expression':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["rsem calculate expression"], pipeline_config)
        elif tool_name.strip().lower() == 'rsem prepare genome':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["rsem prepare genome"], pipeline_config)
        elif tool_name.strip().lower() == 'snpeff annotate':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["snpeff annotate"], pipeline_config)
        elif tool_name.strip().lower() == 'star generate genome index' or tool_name.strip().lower() == 'star generrate genome index':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["star generate genome index"], pipeline_config)
        elif tool_name.strip().lower() == 'star mapping':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["star mapping"], pipeline_config)
        elif tool_name.strip().lower() == 'strelka2 variants caller':
            pipeline_cmd = "bash {}/{} {}".format(config_d['project_base_dir'], config_d["strelka2 variants caller"], pipeline_config)
        else:
            pipeline_cmd = ''
    else:
        pipeline_cmd = ''
    if pipeline_cmd:
        logging.info(pipeline_cmd)
        run_cmd(pipeline_cmd, analysis_dir)
    else:
        with open('{}/Fail.log'.format(analysis_dir), 'w') as fail_f:
            fail_f.write("Please check the pipeline name and the tool name: {}\n".format(pipeline_name))
        logging.error("Please check the pipeline name and the tool name : {}\n".format(pipeline_name))


def main():
    parser = argparse.ArgumentParser(description='输入绝对路径的配置文件config.json')
    parser.add_argument('-i', '--input', required=True, help='input file')
    args = parser.parse_args()
    input_config = args.input
    invoke_pipeline(input_config)


if __name__ == '__main__':
    main()
