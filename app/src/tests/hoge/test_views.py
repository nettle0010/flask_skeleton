import json
import unittest

import pytest

from server import app


@pytest.mark.hoge
class HogeTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_hoge(self):
        response = self.app.get('/hoge/index')
        self.assertEqual(response.status_code, 200)
