import inspect

from pjdby import Build

def _parse_step_config(step):
    # Apply step specific step_config. Defaults are defined in step method level
    if type(step) is dict:  # Step contains additional config
        step_name = step.keys()[0] # Steps should be a dict with one single item
        step_config = step[step_name]
    else:
        step_name = step
        step_config = dict()
    return step_name, step_config

class BuildCXX(object):
    """
    BuildCXX class
    """
    name = 'buildcxx'

    def __init__(self):
        self.build = Build()

    def do(self, task, config):
        steps = config[self.name]['tasks'][task]['steps']
        for step in steps:
            print('-'*80 + '\nRunning step %s' % step)
            step_name, step_config = _parse_step_config(step)

            step_method = getattr(self.build, step_name)               # Get the method
            valid_arguments = inspect.getargspec(step_method).args[1:] # See what arguments from task config are aplicable

            step_resulting_config = {param: (config[param])
                                     for param in valid_arguments
                                     if param in config.keys()}  # Dict with aplicable args
            step_resulting_config.update(step_config)                      # Override with step config
            #self.configure(step_resulting_config)                          # Configure step
            print('DEBUG: Resulting config: %s' % step_resulting_config)

            step_method(**step_resulting_config)                           # Run step
