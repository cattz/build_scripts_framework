
from argparse import ArgumentParser
import yaml
import sys
import inspect
import importlib
import pkg_resources

from pjdby.task_groups import *

def parse_arguments():
    mainparser = ArgumentParser('pyb')
    mainparser.add_argument('group', help='Task group as specified in tasks.yml')
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

def get_task_group_class(group, module='pjdby.task_groups'):
    # For a task to be visible, it has to be imported in tasks/__init__.py
    groups = inspect.getmembers(sys.modules[module], inspect.isclass)
    group_list = dict()
    for gr in groups:
        group_class_name, group_class_object = gr
        group_name = str(group_class_name.lower())  # Convert to lowercase
        # dict with lower case task name and proper class name capitalization
        group_list[group_name] = group_class_name
    return getattr(importlib.import_module(module), group_list[group])

def main():
    args = parse_arguments()
    group = args.group
    task = args.task
    task_definitions = get_config('tasks.yml')
    #global_config = get_config('env.yml')
    print 'Running %s:%s' % (group, task)

    group_config = dict()
    task_config = dict()

    if group not in task_definitions:
        print 'ERROR: group not defined'

    if 'config' in task_definitions[group]:
        group_config = task_definitions[group]['config']

    if task not in task_definitions[group]['tasks']:
        print 'ERROR task %s not defined in group %s' % (task, group)

    if 'config' in task_definitions[group]['tasks'][task]:
        task_config = task_definitions[group]['tasks'][task]['config']

    resulting_config = task_definitions
    resulting_config.update(group_config)
    resulting_config.update(task_config)

    taskGroup = get_task_group_class(group)
    print taskGroup
    tg = taskGroup()
    tg.do(task, resulting_config)

    print resulting_config



if __name__ == '__main__':
    main()
