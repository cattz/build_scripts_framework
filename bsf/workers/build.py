from bsf.pipeline import Pipeline

class BuildCXXWorker(Pipeline):
    """
    Build C++ class, extends Pipeline with build c++ methods
    """
    def __init__(self, source):
        super(BuildCXXWorker, self).__init__(source)
        """ Initializes whatever is needed for C++ builds"""

    def clean(self, folders=None, foo='method'):
        folders = ['build'] if folders is None else folders
        for fld in folders:
            print 'Cleaning %s, using %s config' % (fld, foo)

    def cmake(self, cmake_args):
        print 'cmake %s' % cmake_args

    def make_install(self):
        print 'make install'

    def collect_artifacts(self, origin='build_output', destination='artifacts'):
        print 'Collecting artifacts from "%s" to "%s"' % (origin, destination)
