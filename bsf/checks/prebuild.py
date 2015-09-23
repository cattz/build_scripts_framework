"""Pre-build checks"""

from unittest import TestCase


class PreBuildChecksBase(TestCase):
    type = 'default'

    def test_default_foo(self):
        pass

    def test_default_bar(self):
        pass


class PreBuildChecks(TestCase):
    type = 'optional'

    def test_optional_moo(self):
        pass

    def test_optional_mee(self):
        pass

class PreBuildChecksFoo(TestCase):
    type = 'optional'

    def test_optional_foo(self):
        pass

    def test_optional_fii(self):
        pass