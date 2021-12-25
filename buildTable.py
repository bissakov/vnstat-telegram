#!/usr/bin/python

import json
import datetime

# column width
width = 14

def convertDate(t):
    # month-name day, year
    return(datetime.datetime(t['year'],t['month'],t['day']).strftime('%B %d, %Y'))

def calcPadding(val):
    left = ' ' * (int((width - len(val)) / 2))
    right = ' ' * (width - len(val) - int((width - len(val)) / 2))
    return (left,right)

f = open('data.json')
content = json.load(f)

today = content['interfaces'][0]['traffic']['days'][0]

date = today['date']
rx = today['rx']
tx = today['tx']
total = rx + tx

rx = str(rx) + ' MiB'
rx = calcPadding(rx)[0] + rx + calcPadding(rx)[1]
tx = str(tx) + ' MiB'
tx = calcPadding(tx)[0] + tx + calcPadding(tx)[1]
total = str(total) + ' MiB'
total = calcPadding(total)[0] + total + calcPadding(total)[1]

header = '\n|   Uploaded   |  Downloaded  |    Total     |\n'
linebreak = '|' + '-' * width + '|' + '-' * width + '|' + '-' * width + '|\n'
values = '|' + rx + '|' + tx + '|' + total + '|'

table = header + linebreak + values

message = '*%(date)s*\n```%(table)s```' % {'date': convertDate(date), 'table': table}