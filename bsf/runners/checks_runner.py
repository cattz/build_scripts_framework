import sys
import inspect

class ChecksRunner(object):
    name = 'prebuild'  # Used to match the corresponding key in yaml config

    def __init__(self, source, task_definition, runner_config, task_config):
        self.source = source
        self.config = runner_config
        self.config.update(task_config)
        self.task = task_definition
        self.build = None

    def configure(self):
        pass

    def do(self, task):
        self.configure()
        module = 'bsf.checks.' + self.name

        # Get all classes in module
        all_checks = inspect.getmembers(
            sys.modules[module],
            lambda x: inspect.isclass(x) and x.__module__ == module
        )
        print all_checks

        # Default and optional checks are defined by the attribute 'type' in their test class
        default_check_classes = [ch for _, ch in all_checks if ch.type == 'default']
        optional_check_classes = [ch for _, ch in all_checks if ch.type == 'optional']

        print 'Default: %s' % default_check_classes
        print 'Optional: %s' % optional_check_classes

        # Filter excludes and includes
        if 'exclude' in self.task[task].keys():
            exclude_list = self.task[task]['exclude']
        else:
            exclude_list = None

        if 'include' in self.task[task].keys():
            include_list = self.task[task]['include']
        else:
            include_list = None

        default_checks_to_run = list()
        for chcls in default_check_classes:
            default_checks_to_run += [
                dict(
                    name=test_method,
                    module='%s:%s.%s' % (chcls.__module__, chcls.__name__, test_method),
                    run=test_method not in exclude_list
                )
                for test_method, _ in
                inspect.getmembers(chcls, predicate=inspect.ismethod) if test_method.startswith('test_')
            ]
        print 'ALL:\n%s'
        import pprint
        pprint.pprint(default_checks_to_run)

        optional_checks_to_run = list()
        for chcls in optional_check_classes:
            optional_checks_to_run += [
                dict(
                    name=test_method,
                    module='%s:%s.%s' % (chcls.__module__, chcls.__name__, test_method),
                    run=test_method in include_list
                )
                for test_method, _ in inspect.getmembers(chcls, predicate=inspect.ismethod) if test_method.startswith('test_')
            ]

        pprint.pprint(optional_checks_to_run)