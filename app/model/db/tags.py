
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return f"<Tags(name='{self.name}' )>"
