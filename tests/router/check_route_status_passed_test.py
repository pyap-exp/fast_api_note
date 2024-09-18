import json
from ..base import client
import unittest

token:str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBhdWwifQ.n1jxY8CwTj5VlJt3B_oJZUx_bl49uEmAFWgpHwaCsGA"
class TestSuccess(unittest.TestCase):
    def test_health(self):
        route_health = client.get("/health")
        assert route_health.status_code == 200

    def test_get_all_notes(self):
        res_place_valid = client.get("/notes/all",headers={"X-Token":token})
        assert res_place_valid.status_code == 200

    def test_get_by_id_notes(self):
        res_place_valid = client.get("/notes/2",headers={"X-Token":token})
        assert res_place_valid.status_code == 200
