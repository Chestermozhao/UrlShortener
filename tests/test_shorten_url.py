# -*- coding:utf-8 -*-
import ujson as json
import unittest
import asyncio
from starlette.testclient import TestClient
from url_shortener.database import database, urlshorteners

from url_shortener.main import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def tearDown(self):
        pass

    def test_get_shoteners(self):
        url = "/shortener/"
        rv = self.app.get(url)
        assert rv.status_code == 200

    def test_create_short_path(self):
        url = "/shortener/"
        rv = self.app.post(url, json={"origin_url": "https://stackoverflow.com/"})
        r_content = json.loads(rv._content)
        assert rv.status_code == 200
        assert r_content["status"] == 0
        assert r_content["short_link"].startswith("http://localhost:80")
        assert r_content["origin_url"] == "https://stackoverflow.com/"

        short_link = r_content["short_link"]
        short_path = short_link.split("/")[-1]

        url = "/shortener/"
        rv = self.app.get(url)
        r_content = json.loads(rv._content)
        assert rv.status_code == 200
        assert len(r_content) == 1

        rv = self.app.get(short_path)
        assert rv.status_code == 200

    def test_create_with_failed_url(self):
        url = "/shortener/"
        rv = self.app.post(url, json={"origin_url": "localhost"})
        r_content = json.loads(rv._content)
        assert rv.status_code == 422
        assert r_content["detail"][0]["msg"] == "invalid or missing URL scheme"

    def test_request_failed_url(self):
        loop = asyncio.get_event_loop()
        query = urlshorteners.insert().values(origin_url="12345", short_path="test5")
        loop.run_until_complete(database.execute(query))
        rv = self.app.get("test5")
        r_content = json.loads(rv._content)
        assert rv.status_code == 200
        assert r_content["status"] == -1
        assert r_content["errMsg"] == "request origin url failed"

    def test_empty_short_path(self):
        rv = self.app.get("test6")
        r_content = json.loads(rv._content)
        assert rv.status_code == 200
        assert r_content["status"] == -1
        assert r_content["errMsg"] == "no this short path"


if __name__ == "__main__":
    unittest.main()
