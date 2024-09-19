from fastapi import APIRouter, Depends, HTTPException

from ..dependency.db import database_connect
from ..dependency.header import get_token_header
from ..model.db.notes import Notes
from ..model.serialize.notes import (DataRowNotes, DeleteRowNotes, GetNotes,
                                     NotesBase, get_tags_name)

router = APIRouter(
    prefix="/notes",
    tags=["note"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
async def create_notes(base: NotesBase,sess = Depends(database_connect)):
    return base.save(sess)

@router.put("/update")
async def update_notes(base: DataRowNotes,sess = Depends(database_connect)):
    return base.update(sess)

@router.delete("/delete/{item_id}")
async def delete_notes(item_id: int,sess = Depends(database_connect)):
    base: DeleteRowNotes = DeleteRowNotes(id=item_id)
    return base.delete(sess)

@router.get("/all")
async def get_all_notes(sess = Depends(database_connect))->GetNotes:
    get = sess.query(Notes).all()
    return GetNotes(data=[{"id":x.id,"name":x.name,"content":x.content,"tags":get_tags_name(sess,x.tag_ids)} for x in get])

@router.get("/{item_id}")
async def read_item_by_id(item_id: int,sess = Depends(database_connect))->DataRowNotes:
    get = sess.query(Notes).filter(Notes.id == item_id)
    if get.count() == 0:
        raise HTTPException(status_code=404, detail="Note ID not found")
    return DataRowNotes( **get.one().toObj() )
