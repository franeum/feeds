#!/usr/bin/env python3

DESTROY_RECORD_TABLE = """DROP TABLE IF EXISTS record;"""

CREATE_RECORD_TABLE = """CREATE TABLE record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titledesc blob DEFAULT NULL,
        translated blob DEFAULT NULL,
        compound real DEFAULT NULL,
        date text DEFAULT NULL
    )"""

DB_SIZE = """SELECT COUNT(*) FROM record"""


def INSERT_VALUES(titledesc, translated, compound, date):
    return f"""INSERT INTO record(titledesc, translated, compound, date) VALUES("{titledesc}", "{translated}", "{compound}", "{date}")"""


def SELECT_VALUE(n):
    return f"""SELECT * FROM record WHERE id={n}"""
