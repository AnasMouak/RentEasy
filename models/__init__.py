#!./venv/bin/python
'''
    Package initializer
'''
# Import the FileStorage class from the file_storage module
from models.engine.file_storage import FileStorage

# Import the DBStorage class from the db_storage module
from models.engine.db_storage import DBStorage

# Import the getenv function from the os module
from os import getenv


# If the environment variable RENTEASY_TYPE_STORAGE is set to 'db', create a DBStorage instance
if getenv('RENTEASY_TYPE_STORAGE') == 'db':
    # If the environment variable is set to 'db', use DBStorage
    storage = DBStorage() 
    storage.reload()  # Reload the data from the database
else:
    # If the environment variable is not set to 'db', use FileStorage
    storage = FileStorage() 
    storage.reload() # Reload the data from the file
