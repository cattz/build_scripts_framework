#!/usr/bin/env python


from argparse import ArgumentParser
import yaml
import sys
import os
import inspect
import importlib
#import pkg_resources
from bsf.runners import *

this_dir, _ = os.path.split(__file__)
TEMPLATES_DIR = os.path.join(this_dir, '..', "templates")


def parse_arguments():
    mainparser = ArgumentParser('BSF')
    mainparser.add_argument('runner', help='Runner as specified in tasks.yml')
    mainparser.add_argument('task', help='Task to run as specified in tasks.yml')
    mainparser.add_argument('-s', '--source', default='source', help='Location of source to be build')
    #mainparser.add_argument('--user', help='User name. Will use this credentials whenever is needed')
    #mainparser.add_argument('--password', help='Password')
    return mainparser.parse_args()


def get_config(cfg):
    with open(cfg, 'r') as stream:
        return yaml.load(stream)


def flatten_dict(dd, separator='_', prefix=''):
    return {str(prefix) + separator + str(k) if prefix else k: v
            for kk, vv in dd.items()
            for k, v in flatten_dict(vv, separator, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}


def get_runner_class(group, module='bsf.runners'):
    # For a task to be visible, it has to be imported in tasks/__init__.py
    groups = inspect.getmembers(sys.modules[module], inspect.isclass)
    group_list = dict()
    for gr in groups:
        group_class_name, group_class_object = gr
        group_name = str(group_class_name.lower())  # Convert to lowercase
        # dict with lower case task name and proper class name capitalization
        group_list[group_name] = group_class_name
    return getattr(importlib.import_module(module), group_list[group])

def get_resulting_task_config(default_tasks, runner_config, task_config):
    """
    Returns the  resulting by overriding
    :param default_tasks: 
    :param runner_config: 
    :param task_config: 
    :return:
    """
    resulting_config = default_tasks
    resulting_config.update(runner_config)
    resulting_config.update(task_config)
    return resulting_config

def main():
    args = parse_arguments()
    runner = args.runner
    task = args.task
    default_tasks = get_config(os.path.join(TEMPLATES_DIR, 'tasks.yml'))
    #global_config = get_config('env.yml')

    print 'Running %s:%s' % (runner, task)

    runner_config = dict()
    task_config = dict()

    if runner not in default_tasks:
        print 'ERROR: runner not defined in tasks'
        sys.exit(-1)
    if task not in default_tasks[runner]['tasks']:
        print 'ERROR task %s not defined in runner %s' % (task, runner)
        sys.exit(-1)

    task_definition = {tsk: default_tasks[runner]['tasks'][tsk] for tsk in default_tasks[runner]['tasks'] if tsk == task}

    if 'config' in default_tasks[runner]:
        runner_config = default_tasks[runner]['config']

    if 'config' in default_tasks[runner]['tasks'][task]:
        task_config = default_tasks[runner]['tasks'][task]['config']

    runnerClass = get_runner_class(runner)
    rnr = runnerClass(args.source, task_definition, runner_config, task_config)
    rnr.do(task)

if __name__ == '__main__':
    main()
