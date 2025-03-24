#!/usr/bin/env python3

import datetime
import locale


def string2date(s):
    """English date string to datetime format"""
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return datetime.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S %z")


def date2italian(dt):
    """datetime format to Italian string"""
    locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
    return dt.strftime("%A, %d %B %Y, %H:%M").title()
