import unittest
import json
from flask import current_app
from app import create_app, db


# 接收请求--》创建请求上下文--》请求上下文入栈--》创建该请求的应用上下文--》应用上下文入栈--》处理逻辑--》请求上下文出栈--》应用上下文出栈
class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("default" or "testing")
        self.app_context = self.app.app_context()  # 显示的生成应用上下文
        self.app_context.push()  # 调用应用上下文
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    # def test_app_exists(self):
    #     self.assertFalse(current_app is None)
    #
    # def test_app_is_testing(self):
    #     self.assertTrue(current_app.config["TESTING"])


if __name__ == "__main__":
    unittest.main()
