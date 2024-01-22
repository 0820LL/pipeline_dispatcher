#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import subprocess
import sys

def read_json(json_f):
    import json
    import sys
    try:
        with open(json_f, 'r') as in_f:
            json_d = json.load(in_f)
            return json_d
    except IOError as e:
        logging.error(e)
        logging.error("Cannot open config.json file: {}".format(json_f))
        sys.exit(1)


def get_task_id(json_f):
    json_d = read_json(json_f)
    task_id = json_d["taskId"]
    return task_id


def get_script_path(json_f):
    json_d = read_json(json_f)
    script_path = json_d["script_path"]
    return script_path


def get_pipeline_name(json_f):
    json_d = read_json(json_f)
    pipeline = json_d["pipeline"]
    return pipeline


def run_cmd(cmd, analysis_dir):
    obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stat = obj.wait()
    logging.info('subprocess.Popen stat: {}'.format(str(stat)))
    if stat:
        err_info = obj.stderr.read()
        try:
            with open('{}/Fail.log'.format(analysis_dir), 'w') as fail_f:
                fail_f.write("Running Command: '{0}' is failed. \n{1}\n".format(cmd, err_info))
            logging.error("Running Command: '{0}' is failed. \n{1}\n".format(cmd, err_info))
        except IOError as e:
            logging.error('fail to make log file : {}'.format(analysis_dir))
        sys.exit(1)


def check_call(cmd, ana_dir):
    import subprocess
    #logger = logging.getLogger(__name__)
    with open("{}/Run.log".format(ana_dir), "w") as out_f:
        out_f.write('Running CMD: "' + cmd + '"  ...')
    # print('Running CMD: "' + cmd + '"  ...')
    # if subprocess.check_call(cmd, shell=True) != 0:
    #    print("ERROR running cmd: {0}.".format(cmd))
    #    print(sys.stdout)
    #    sys.exit(-1)
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        with open("{}/Fail.log".format(ana_dir), "w") as out_f:
            out_f.write(str(e))


'''
def run_status(cmd, analysis_dir):
    import sys
    import subprocess

    if subprocess.check_call(cmd, shell=True) == 0:
        try:
            with open('{}/success.log'.format(analysis_dir), 'w') as out_f:
                out_f.write("Running Command: '{0}' is success.".format(cmd))
        except IOError as e:
            print(e)
            print('Cannot write success file.')
            sys.exit(1)
    else:
        try:
            with open('{}/fail.log'.format(analysis_dir), 'w') as out_f:
                out_f.write("Running Command: '{0}' is failed.".format(cmd))
        except IOError as e:
            print(e)
            print('Cannot write failed file.')
            sys.exit(1)
'''
