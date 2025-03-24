#!/usr/bin/env python3

import sqlite3 as sql
import binascii
from sql_commands import *

DB_PATH = "./data/records.db"
CONNECTION = None
CURSOR = None


def connect():
    """return CURSOR to db CONNECTION"""
    global CURSOR, CONNECTION
    CONNECTION = sql.connect(DB_PATH)
    CURSOR = CONNECTION.cursor()


def record_table_create():
    CURSOR.execute(CREATE_RECORD_TABLE)


def record_table_destroy():
    CURSOR.execute(DESTROY_RECORD_TABLE)


def insert_value(titledesc, translated, compound, date):
    _title = hex_encode(titledesc)
    _translated = hex_encode(translated)

    try:
        CURSOR.execute(INSERT_VALUES(_title, _translated, compound, date))
        print(f"inserted")
    except sql.IntegrityError:
        print("ERROR")
    except Exception as e:
        print(e)

    return None


def get_size():
    to_fetch = CURSOR.execute(DB_SIZE)
    fetched = to_fetch.fetchone()[0]
    return fetched


def get_value_by_id(idx):
    print("Indice richiesto:", idx)
    to_fetch = CURSOR.execute(SELECT_VALUE(idx))
    fetched = to_fetch.fetchone()

    if fetched:
        data = {}
        data['title'] = hex_decode(fetched[1])
        data['translated'] = hex_decode(fetched[2])
        data['compound'] = fetched[3]
        data['date'] = fetched[4]

    return data


def commit():
    CONNECTION.commit()


def hex_encode(s):
    return binascii.hexlify(bytes(s, 'utf-8'))


def hex_decode(s):
    try:
        str_to_bytes = eval(s)
        decoded = binascii.unhexlify(str_to_bytes).decode('utf-8')
    except:
        decoded = ''

    return decoded


def init():
    connect()
    record_table_destroy()
    record_table_create()


def close():
    CONNECTION.close()
