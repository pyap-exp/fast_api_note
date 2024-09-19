import re
from typing import List

from fastapi import HTTPException
from pydantic import BaseModel, field_validator

from ..db.notes import Notes
from ..db.tags import Tags


def get_tags_name(session,list_tags_int):
    if list_tags_int is None:
        return []
    raw = []
    get_all = session.query(Tags).filter(Tags.id.in_(list_tags_int)).all()
    for val in get_all:
        raw.append(val.name)
    return raw

def upsert_get_tags(session,list_tags_str:List[str]) ->List[int]:
    raw:List[int] = []

    for val in list_tags_str:
        get = session.query(Tags).filter(Tags.name == val)
        if get.count() == 0:
            ed_insert = Tags(name=val)
            session.add(ed_insert)
            session.commit()
            raw.append(ed_insert.id)
        else:
            raw.append(get.one().id)

    return raw

class _NotesId(BaseModel):
    id: int

class NotesBase(BaseModel):
    name:str
    content:str
    tags:List[str]=[]

    @field_validator("tags")
    def validate_tags_format(cls, value):
        for val in value:
            search = re.search(r"^([a-zA-Z0-9\-\_]{2,})$", val)
            if search is None:
                raise ValueError("`tags` must follow ^([a-zA-Z0-9-_]{2,})$")
        return value
    def save(self,session):
        ed_insert = Notes(name=self.name,
            content=self.content,
            tag_ids= upsert_get_tags(session,self.tags))
        session.add(ed_insert)
        session.commit()
        return {
            "message": "Save successfully"
        }

class DataRowNotes(_NotesId,NotesBase):
    def update(self,session):
        get = session.query(Notes).filter(Notes.id == self.id)
        if get.count() == 0:
            raise HTTPException(status_code=404, detail="Note ID not found for update")
        get.update({
            "name":self.name,
            "content":self.content,
            "tag_ids":upsert_get_tags(session,self.tags)
        })
        session.commit()
        return {
            "message": "Save successfully"
        }


class DeleteRowNotes(_NotesId):

    def delete(self,session):
        get = session.query(Notes).filter(Notes.id == self.id)
        if get.count() == 0:
            raise HTTPException(status_code=404, detail="Note ID not found for delete")
        get.delete()
        session.commit()
        return {
            "message": "Delete successfully"
        }
class GetNotes(BaseModel):
    data:List[DataRowNotes]
