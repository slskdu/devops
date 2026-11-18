import os
import unittest

os.environ.pop("REDIS_HOST", None)

import app as guestbook  # noqa: E402


class GuestbookTest(unittest.TestCase):
    def setUp(self):
        guestbook.app.config["TESTING"] = True
        guestbook._memory_entries.clear()
        self.client = guestbook.app.test_client()

    def test_healthz(self):
        res = self.client.get("/healthz")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["status"], "ok")

    def test_readyz_memory_mode(self):
        res = self.client.get("/readyz")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["status"], "ready")

    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_add_entry(self):
        res = self.client.post("/add", data={"name": "철수", "message": "안녕하세요"})
        self.assertEqual(res.status_code, 302)
        data = self.client.get("/api/entries").get_json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["entries"][0]["name"], "철수")
        self.assertEqual(data["entries"][0]["message"], "안녕하세요")

    def test_empty_message_ignored(self):
        self.client.post("/add", data={"name": "철수", "message": "   "})
        data = self.client.get("/api/entries").get_json()
        self.assertEqual(data["count"], 0)

    def test_anonymous_name(self):
        self.client.post("/add", data={"message": "이름 없이"})
        data = self.client.get("/api/entries").get_json()
        self.assertEqual(data["entries"][0]["name"], "익명")


if __name__ == "__main__":
    unittest.main()
