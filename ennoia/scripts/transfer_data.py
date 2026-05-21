"""
Copies a database table that already exists into another table that already exists.

Specify the table that you want to copy in 'source_db' and specify the table that you want to receive the copy from in 'target_db'.
"""

import sqlite3

source_db = sqlite3.connect('/home/jaketanis/ennoia/instance/bookshelf.sqlite')
target_db = sqlite3.connect('/home/jaketanis/ennoia/instance/ennoia.sqlite')

source_db.backup(target_db)
source_db.close()
target_db.close()

