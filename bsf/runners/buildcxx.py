
from bsf.workers import BuildCXXWorker
from bsf.runners import Runner


class BuildCXX(Runner):
    """
    BuildCXX class
    """

    def configure(self):
        self.pipeline = BuildCXXWorker(source=self.source)
        self.pipeline.version = '3.4.5'

