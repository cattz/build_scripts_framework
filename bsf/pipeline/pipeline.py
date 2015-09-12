"""Pipeline general class. All heavy lifting is done here"""
from pipeline_config import PipelineConfig

class Pipeline(PipelineConfig):

    def __init__(self, source):
        super(Pipeline, self).__init__(source)

