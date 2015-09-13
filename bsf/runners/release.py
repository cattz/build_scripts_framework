
from bsf.runners import Runner
from bsf.workers import ReleaseWorker
from bsf.managers import Artifactory


class Release(Runner):
    """Release runner
    """
    name = 'release'

    def configure(self):
        self.pipeline = ReleaseWorker(source=self.source)
        self.pipeline.binary_repo = Artifactory(url='http://foo.bar')

