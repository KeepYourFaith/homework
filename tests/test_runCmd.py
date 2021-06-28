import json
import unittest
from tests.test_basics import BasicTestCase


class RunCmdTestCase(BasicTestCase):
    def test_run_cmd(self):
        response = self.client.post("/cmd", data={"cmd": "ls -al"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_empty_cmd(self):
        response = self.client.post("/cmd", data={"cmd": ""})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 200001)

    def test_too_long_cmd(self):
        response = self.client.post("/cmd", data={"cmd": "号"* 15520})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print("12345", resp_dict.get("message"))
        self.assertEqual(code, 200002)

    def test_invalid_cmd(self):
        response = self.client.post("/cmd", data={"cmd": "la--" })
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print("12345", resp_dict.get("message"))
        self.assertEqual(code, 200003)


if __name__ == "__main__":
    unittest.main()
