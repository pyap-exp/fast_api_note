from typing import Annotated

import jwt
from fastapi import Header, HTTPException

async def get_token_header(x_token: Annotated[str, Header()]):
    try:
        jwt.decode(x_token, "secret", algorithms=["HS256"])
    except Exception as exc:
        raise HTTPException(status_code=400, detail="X-Token header invalid") from exc

async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
