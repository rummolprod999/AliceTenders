import os
import sqlite3

DBNAME = 'alice.sqlite'


def create_db_if_notexist():
    if not os.path.exists(DBNAME):
        open(DBNAME, 'a').close()
        conn = sqlite3.connect(DBNAME)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE `avito` (
 `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
 `id_av` TEXT,
 `price` TEXT
)""", )
        conn.commit()
        cursor.execute("""CREATE INDEX `id_av` ON `avito` (
 `id_av`
)""", )
        conn.commit()
        cursor.execute("""CREATE INDEX `price` ON `avito` (
 `price`
)""", )
        conn.commit()
        cursor.execute("""CREATE INDEX `prim` ON `avito` (
`id`
)""", )
        conn.commit()
        cursor.close()
        conn.close()
