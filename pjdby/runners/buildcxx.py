import inspect

from pjdby.runners import Runner

from pjdby import Build



class BuildCXX(Runner):
    """
    BuildCXX class
    """
    name = 'buildcxx'

    def configure(self):
        super(BuildCXX, self).configure()
        self.build.artifactory = 'Artifatory C++'

