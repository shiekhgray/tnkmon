#################################################
#                   TNKMON
#
# A small aquarium monitor and control package
# designed to be run on a raspberry pi
#
# Written by Graham McCullough
#
#################################################

import os
#import RPi.GPIO as gpio
from sqlite3 import dbapi2 as sqlite
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

tnkmon = Flask(__name__)

tnkmon.config.update(dict(
    DATABASE=os.path.join(tnkmon.root_path, 'tnkmon.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

tnkmon.config.from_envvar('TNKMON_SETTINGS', silent=True)

def connect_database():
    """Connects to the local db."""
    row = sqlite.connect(tnkmon.config['DATABASE'])
    row.row_factory = sqlite.Row
    return row

def init_database():
    """Initializes local db"""
    database = get_database()
    with tnkmon.open_resource('schema.sql', mode='r') as f:
        database.cursor().executescript(f.read())
    database.commit()

def get_database():
    """Opens a new database connection if there isn't one yet open
        in the context."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_database()
    return g.sqlite_db

@tnkmon.teardown_appcontext
def close_database(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@tnkmon.route('/')
def home():
    return "Coming soon!"

@tnkmon.route('/webcam')
def webcam():
    return "Coming soon!"

@tnkmon.route('/lights')
def lights():
    return "Coming soon!"

@tnkmon.route('/co2')
def co2():
    return "Coming soon!"


if __name__ == "__main__":
    tnkmon.run()
