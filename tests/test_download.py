import json
import unittest
from tests.test_basics import BasicTestCase


class DownloadTestCase(BasicTestCase):
    def test_download_file(self):
        response = self.client.post("/download/0", data={"address": "http://www.rarlab.com/rar/rarlinux-3.8.0.tar.gz"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_cover_download_exist_file(self):
        response = self.client.post("/download/1", data={"address": "http://www.rarlab.com/rar/rarlinux-3.8.0.tar.gz"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_invalid_url(self):
        response = self.client.post("/download/0", data={"address": "http://a456.com"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 100000)

    def test_uncover_download_exist_file(self):
        response = self.client.post("/download/0", data={"address": "http://www.rarlab.com/rar/rarlinux-3.8.0.tar.gz"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 100005)

    def test_empty_url(self):
        response = self.client.post("/download/0", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 100006)

    def test_too_long_url(self):
        response = self.client.post("/download/0", data={"address": "http://" + "0"*10000})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 100007)


if __name__ == "__main__":
    unittest.main()
