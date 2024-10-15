#!/usr/bin/python
"""Instatiates the storage object.
-> if the environmental variable HBnb_TYPE_STORAGE is set 
to db.
-> instatiates the database storage engine(DBStorage).
-> otherwise instatiate the file storage 
engine(fileStorage).
"""

from os import getenv

if getenv("HBnb_TYPE_STORAGE") == "db":
    from models.engine.db_storage
import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage
import FileStorage
    storage = FileStorage()
storage.reload()

