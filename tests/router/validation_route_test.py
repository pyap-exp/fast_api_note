import json
from ..base import client
import unittest

token:str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBhdWwifQ.n1jxY8CwTj5VlJt3B_oJZUx_bl49uEmAFWgpHwaCsGA"
class ValidationRouteTest(unittest.TestCase):
    def test_invalid_tags(self):

        res_place = client.post("/notes/create",json={
          "name": "string",
          "content": "string",
          "tags": ["asd asd"]
        },headers={"X-Token":token})
        assert res_place.status_code == 422

    def test_valid_tags(self):

        res_place_valid = client.post("/notes/create",json={
          "name": "string",
          "content": "string",
          "tags": ["asdasd"]
        },headers={"X-Token":token})
        assert res_place_valid.status_code == 200
