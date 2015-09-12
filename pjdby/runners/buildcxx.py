
from pjdby.workers import BuildCXXWorker
from pjdby.runners import Runner


class BuildCXX(Runner):
    """
    BuildCXX class
    """

    def configure(self):
        self.build = BuildCXXWorker(source=self.source)
        self.build.version = '3.4.5'

