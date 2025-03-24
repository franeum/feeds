#!/usr/bin/env python3

from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("http://127.0.0.1:5000")


def translate(sentence):
    "translate ita-eng"
    return lt.translate(sentence, "it", "en")
