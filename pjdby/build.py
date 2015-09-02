class Build(object):
    """
    Build class
    """
    def __init__(self):
        pass

    def clean(self, folders):
        for fld in folders:
            print 'Cleaning %s' % fld

    def cmake(self, cmake_args):
        print 'cmake %s' % cmake_args
