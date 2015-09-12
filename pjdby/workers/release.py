
from pjdby.pipeline import Pipeline


class ReleaseWorker(Pipeline):
    """
    Release class extends the base Pipeline with release methods
    """
    def __init__(self, source):
        super(ReleaseWorker, self).__init__(source)

    def publish(self, path, properties=None):
        """Publish artifacts to an artifact repository
        """
        print 'Publishing to path %s with properties %s' % (path, properties)
        print self.binary_repo

    def promote(self, repo, properties=None):
        """Promotes artifacts
        """
        print 'Publishing to repo %s with properties %s' % (repo, properties)
