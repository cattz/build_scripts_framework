
class Artifactory(object):
    """Artifactory manager class"""

    def __init__(self, url='http://default.artifactory.url/artifactory'):
        self.url = url

    def publish(self, local_path, repo, remote_path, properties=None):
        print 'Manager: Publishing {local} to {remote} (server: {url}/{repo})'.format(
            local=local_path,
            remote=remote_path,
            repo=repo,
            url=self.url
        )
        print 'Properties: %s' % properties

    def promote(self, origin_repo, promotion_repo, build=None, remote_path=None):
        print 'Promoting from {orepo} to {drepo}'.format(
            orepo=origin_repo,
            drepo=promotion_repo
        )
