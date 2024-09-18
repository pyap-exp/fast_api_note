
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    content = Column(String)
    tag_ids = Column(ARRAY(Integer))


    def __repr__(self):
        return f"<Notes(name='{self.name}' )>"
    def toObj(self):
        return {
            "id":self.id,
            "name":self.name,
            "content":self.content,
            "tag_ids":self.tag_ids,
        }
