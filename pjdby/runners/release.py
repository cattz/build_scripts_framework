
from pjdby.runners import Runner

from pjdby.workers import ReleaseWorker


class Release(Runner):
    """
    BuildCXX class
    """
    name = 'buildcxx'

    def configure(self):
        self.build = ReleaseWorker(source=self.source)
        self.build.binary_repo = 'Artifatory C++'

