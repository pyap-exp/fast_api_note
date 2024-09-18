from fastapi import APIRouter, Depends, HTTPException

from ..dependency.db import database_connect
from ..dependency.header import get_token_header
from ..model.db.notes import Notes
from ..model.db.tags import Tags
from ..model.serialize.notes import GetNotes, get_tags_name
from ..model.serialize.tag import GetAllTags

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/all")
async def get_all_tag(sess = Depends(database_connect))->GetAllTags:
    get = sess.query(Tags).all()
    return GetAllTags(data=[{"id":x.id,"name":x.name} for x in get])

@router.get("/{name}")
async def read_item_by_tag_nam(name: str,sess = Depends(database_connect))->GetNotes:
    get = sess.query(Tags).filter(Tags.name == name)
    if get.count() == 0:
        raise HTTPException(status_code=404, detail="Tag name not found")
    get = sess.query(Notes).filter(Notes.tag_ids.contains([get.one().id])).all()
    return GetNotes(data=[{"id":x.id,"name":x.name,"content":x.content,"tags":get_tags_name(sess,x.tag_ids)} for x in get])
