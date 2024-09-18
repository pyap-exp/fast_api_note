import jwt
from fastapi import APIRouter

from ..model.serialize.user import GetUserAuth, UserAccess

router = APIRouter()

@router.post("/getaccess/", tags=["users"])
async def get_access(user:UserAccess)->GetUserAuth:
    token = jwt.encode({"username": user.name}, "secret", algorithm="HS256")
    return GetUserAuth(token=token)
