class Build(object):
    """
    Build class
    """
    def __init__(self):
        self.artifactory = None

    def clean(self, folders=None, foo='method'):
        folders = ['default'] if folders is None else folders
        for fld in folders:
            print 'Cleaning %s, using %s config' % (fld, foo)

    def cmake(self, cmake_args):
        print 'cmake %s' % cmake_args

    def make_install(self):
        print 'make install'

    def collect_artifacts(self, dir_from='build_output'):
        print 'Collecting artifacts from "%s"' % dir_from
