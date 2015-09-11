import yaml

def get_config(cfg):
    with open(cfg, 'r') as stream:
        in_task = stream.read()
        print in_task
        out_task = in_task.replace('<BEER>', 'wine')
        return yaml.load(out_task)


print get_config('foo.yml')