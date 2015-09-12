"""Base pipeline initialization and configuration"""

import os


class PipelineConfig(object):

    def __init__(self, source):
        self.source = source  #: Source code folder
        self.build_number = os.environ.get('bamboo_buildNumber')
        self.vcs = None  #: Version control manager
        self.binary_repo = None  #: Binary repository manager, ie: Artifactory

    def init_vcs(self):
        """Initialize VCS manager from environment and/or info from source folder
        """
        pass
