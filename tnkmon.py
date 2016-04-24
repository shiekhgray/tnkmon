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
import sqlite3 
import datetime
import tnkcron
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


#######
# create Flask app
#######
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
    #link to lights
    #link to CO2
    #show webcam capture if lights are on
    return render_template('page.html', content="coming soon")

@tnkmon.route('/webcam')
def webcam():
    #just run webcam-streamer to the browser
    return render_template('page.html', content="coming soon")


@tnkmon.route('/lights')
def lights():
    #turn lights on
    #turn lights off
    #automatic schedule
    #color schedule?
    light_status = tnkcron.db('light')
    return render_template('page.html', content=light_status)

@tnkmon.route('/co2')
def co2():
    #Turn on CO2 (only if lights are on)
    #Turn off CO2 (automatically if lights are off)
    #schedule
    co2_status = tnkcron.db('co2')
    return render_template('page.html', content=co2_status)


@tnkmon.route('/timelapses')
def timelapses():
    #do a daily timelapse
    #show all previous timelapses.
    return render_template('page.html', content="coming soon")



if __name__ == "__main__":
    tnkmon.run()
