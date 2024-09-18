from sqlalchemy.orm import declarative_base

from .helper.db import engine
from .model.db.notes import Notes
from .model.db.tags import Tags

Base = declarative_base()

if __name__ == "__main__":
    print("create db")
    Base.metadata.create_all(engine, [Notes.__table__,Tags.__table__])
