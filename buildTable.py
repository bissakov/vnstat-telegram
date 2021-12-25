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
rx = today['rx'] / 1000
tx = today['tx'] / 1000
total = (today['rx'] + today['tx']) / 1000

rxConverted = round(today['rx'] / 1024, 3)
txConverted = round(today['tx'] / 1024, 3)
totalConverted = round((today['rx'] + today['tx']) / 1024, 3)

rx = str(rx) + ' MB'
rx = calcPadding(rx)[0] + rx + calcPadding(rx)[1]
tx = str(tx) + ' MB'
tx = calcPadding(tx)[0] + tx + calcPadding(tx)[1]
total = str(total) + ' MB'
total = calcPadding(total)[0] + total + calcPadding(total)[1]

rxConverted = str(rxConverted) + ' MiB'
rxConverted = calcPadding(rxConverted)[0] + rxConverted + calcPadding(rxConverted)[1]
txConverted = str(txConverted) + ' MiB'
txConverted = calcPadding(txConverted)[0] + txConverted + calcPadding(txConverted)[1]
totalConverted = str(totalConverted) + ' MiB'
totalConverted = calcPadding(totalConverted)[0] + totalConverted + calcPadding(totalConverted)[1]

header = '\n|   Uploaded   |  Downloaded  |    Total     |\n'
linebreak = '|' + '-' * width + '|' + '-' * width + '|' + '-' * width + '|\n'
valuesBytes = '|' + rx + '|' + tx + '|' + total + '|\n'
valuesBibytes = '|' + rxConverted + '|' + txConverted + '|' + totalConverted + '|'

table = header + linebreak + valuesBytes + valuesBibytes

message = '*%(date)s*\n```%(table)s```' % {'date': convertDate(date), 'table': table}