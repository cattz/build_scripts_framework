from unittest import TestCase
from bsf.runners import ChecksRunner

from bsf.checks import *

__author__ = 'xabierdavila'


class TestChecksRunner(TestCase):
    def test_do(self):
        task_definition = dict(
            prebuild=dict(
                exclude=['test_default_foo'],
                include=['test_optional_mee']
            )
        )
        runner = ChecksRunner('source',
                              task_definition,
                              dict(), dict())

        runner.do('prebuild')
