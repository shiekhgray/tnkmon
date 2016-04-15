#!/usr/bin/env python

import sqlite3
import os

print("Building local sqlite3 database")

###############################################3
cwd = os.getcwd()
print(cwd)

conn = sqlite3.connect(cwd + '/tnkmon.db')

with conn:
    cursor = conn.cursor()

    ####reset table
    cursor.execute("DROP TABLE IF EXISTS webctl")

    cursor.execute("CREATE TABLE webctl (key TEXT, value FLOAT)")
    cursor.execute("INSERT INTO webctl VALUES('light_on_start', 9)")
    cursor.execute("INSERT INTO webctl VALUES('light_on_dur', 8)")
    cursor.execute("INSERT INTO webctl VALUES('co2_on_start', 9)")
    cursor.execute("INSERT INTO webctl VALUES('co2_on_dur', 6)")
