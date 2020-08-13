# -*- coding:utf-8 -*-
import unittest
from starlette.testclient import TestClient

from url_shortener.main import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def tearDown(self):
        pass

    def test_swagger_doc(self):
        url = "/"
        rv = self.app.get(url)
        assert rv.status_code == 200


if __name__ == "__main__":
    unittest.main()
