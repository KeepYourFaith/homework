import json
import unittest
from tests.test_basics import BasicTestCase


class HistoryTestCase(BasicTestCase):
    def test_history_get(self):
        response = self.client.get("/history/1")
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        first_id = resp_dict.get("message")["result"][0]["id"]
        self.assertEqual(first_id, 1)

    def test_history_post(self):
        response = self.client.post("/history/3", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        first_id = resp_dict.get("message")["result"][0]["id"]
        self.assertEqual(first_id, 1)

    def test_history_get_critical(self):
        response = self.client.get("/history/7", )
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_history_post_critical(self):
        response = self.client.post("/history/7", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_search_by_ip(self):
        ip_addr = "127.0.0.1"
        response = self.client.post("/history/1", data={"ip_addr": ip_addr})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        first_id = resp_dict.get("message")["result"][0]["ip_address"]
        self.assertEqual(first_id, ip_addr)

    def test_search_by_begin_time(self):
        response = self.client.post("/history/1", data={"begin_time": "2021-6-27 13:13"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_search_by_end_time(self):
        response = self.client.post("/history/1", data={"end_time": "2021-6-27 13:13"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        first_id = resp_dict.get("message")["result"][0]["id"]
        self.assertEqual(first_id, 1)

    def test_search_by_code(self):
        true_code = 0
        response = self.client.post("/history/1", data={"ret_code": true_code})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        for i in resp_dict.get("message")["result"]:
            expect_code = i["ret_code"]
        self.assertEqual(expect_code, true_code)

    def test_search_by_begin_end_time(self):
        response = self.client.post("/history/1", data={"begin_time": "2021-6-27 13:13", "end_time": "2021-6-28 14:00"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_search_by_any(self):
        response = self.client.post("/history/1", data={"begin_time": "2021-6-27 13:13", "end_time": "2021-6-28 14:00", "ret_code": 0})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_post_get_excess(self):
        self.client.post("/history/1",data={"ret_code": 0})
        response = self.client.get("/history/20")
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)
        first_id = resp_dict.get("message")["result"][0]["id"]
        self.assertEqual(first_id, 1)

    def test_post_get_unexcess(self):
        self.client.post("/history/2", data={"ret_code": 0})
        response = self.client.get("/history/2")
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_too_long_ip(self):
        response = self.client.post("/history/2", data={"ip_addr": "0"*10000})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 300001)

    def test_begin_time_to_year(self):
        response = self.client.post("/history/2", data={"begin_time": "2022"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_begin_time_to_month(self):
        response = self.client.post("/history/2", data={"begin_time": "2021-01"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_begin_time_to_day(self):
        response = self.client.post("/history/2", data={"begin_time": "2021-06-28"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_begin_time_to_hour(self):
        response = self.client.post("/history/1", data={"begin_time": "2021-06-28 14"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_begin_greater_end(self):
        response = self.client.post("/history/1", data={"begin_time": "2021-06-28 14", "end_time":"2021-09"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_error_data(self):
        response = self.client.post("/history/1", data={"begin_time": "abc"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)

    def test_error_ip(self):
        response = self.client.post("/history/1", data={"ip_addr": "abc"})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("code", resp_dict)
        code = resp_dict.get("code")
        print(resp_dict.get("message"))
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
