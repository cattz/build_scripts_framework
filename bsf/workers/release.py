
from bsf.pipeline import Pipeline


class ReleaseWorker(Pipeline):
    """
    Release class extends the base Pipeline with release methods
    """
    def __init__(self, source):
        super(ReleaseWorker, self).__init__(source)

    def publish(self, path, properties=None):
        """Publish artifacts to an artifact repository
        """
        default_properties = {
            'publish.date': '23/8/2015',
            'publish.time': '17:45:30'

        }
        props = default_properties.update(properties) if properties else default_properties
        print 'Worker: Publishing to path %s with properties %s' % (path, props)
        self.binary_repo.publish('artifacts', 'ci-repo', 'org/prod')

    def promote(self, repo, properties=None):
        """Promotes artifacts
        """
        print 'Publishing to repo %s with properties %s' % (repo, properties)
