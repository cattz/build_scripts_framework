class Build(object):
    """
    Build class
    """
    def __init__(self):
        pass

    def clean(self, folders=['default']):
        for fld in folders:
            print 'Cleaning %s' % fld

    def cmake(self, cmake_args):
        print 'cmake %s' % cmake_args

    def make_install(self):
        print 'make install'

    def collect_artifacts(self, dir_from='build_output'):
        print 'Collecting artifacts from "%s"' % dir_from
