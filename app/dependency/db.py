from typing import Any

import redis

from ..helper.db import session


def redis_connect()->Any:
    return redis.Redis(host="localhost", port=6379, decode_responses=True)

def database_connect()->Any:
    return session
