#!/usr/bin/env python
import wiringpi as gpio
import time
import os
import sqlite3
import datetime

gpio.wiringPiSetup()
light_pin = 0
co2_pin = 7

#connect to DB
def db(query):
    cwd = os.getcwd()
    conn = sqlite3.connect(cwd + '/tnkmon.db')

    time = datetime.datetime.now()
    hour_now = time.hour
    min_now = float(time.minute)
    min_percent = min_now / 60
    now = float(hour_now+min_percent)

    if query == "light":
        with conn:
            ####Build cursor
            cursor = conn.cursor()

            ####Get lights information
            cursor.execute("SELECT value FROM webctl WHERE key='light_on_start'")
            light_on_start = cursor.fetchall()
            cursor.execute("SELECT value FROM webctl WHERE key='light_on_dur'")
            light_on_dur = cursor.fetchall()

            light_start = light_on_start[0][0]
            light_end = light_on_start[0][0] + light_on_dur[0][0]

            light = "off"

            if now >= light_start and now < light_end:
                light = "on"

        return light

    if query == "co2":
        with conn:
            ####Build cursor
            cursor = conn.cursor()

            ####Get CO2 information
            cursor.execute("SELECT value FROM webctl WHERE key='co2_on_start'")
            co2_on_start = cursor.fetchall()
            cursor.execute("SELECT value FROM webctl WHERE key='co2_on_dur'")
            co2_on_dur = cursor.fetchall()

            co2_start = co2_on_start[0][0]
            co2_end = co2_on_start[0][0] + co2_on_dur[0][0]

            co2 = "off"

            if now >= co2_start and now < co2_end:
                co2 = "on"

        return co2

    else:
        return "query not recognized"

def set_plug_state(plug, set_state):
    if plug == "light":
        pin = light_pin
    elif plug == "co2":
        pin = co2_pin
    else:
        raise LookupError("Error: " + plug + " is an unrecognized control pin; expects 'light' or 'co2'.")

    if set_state == "on":
        state = 0
    elif set_state == "off":
        state = 1
    else:
        raise LookupError("Error: " + state + " is an unrecognized state; expects 'on' or 'off'.")

    gpio.digitalWrite(pin, state)
