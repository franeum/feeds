#!/usr/bin/env python3

import db
from random import randint
import format_data as fd

db.connect()

DB_SIZE = db.get_size()
SEPARATOR = 100

for _ in range(25):
    one = db.get_value_by_id(randint(1, DB_SIZE))

    date = one['date']
    form_date = fd.date2italian(fd.string2date(date))
    print()
    print('=' * SEPARATOR)
    print(form_date)
    print('-' * SEPARATOR)
    print(one['title'])
    print('-' * SEPARATOR)
    print(one['compound'])
    print('=' * SEPARATOR)
    print()
