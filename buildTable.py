#!/usr/bin/python

import json
import datetime

# column width
width = 16

def convertDate(t):
    # month-name day, year
    return(datetime.datetime(t['year'],t['month'],t['day']).strftime('%B %d, %Y'))

def calcPadding(val):
    left = ' ' * (int((width - len(val)) / 2))
    right = ' ' * (width - len(val) - int((width - len(val)) / 2))
    return (left,right)

def convertBytes(val, t):
    unit = 'B' if t == 1000 else 'iB'
    val = round(val / t, 2)

    if (val >= 1000 and val < 1000000):
        return str(round(val / t, 2)) + ' G' + unit
    elif (val >= 1000000):
        return str(round(val / (t * t), 2)) + ' T' + unit

    return str(val) + ' M' + unit

def remap(value):
    # return (value - oldRangeMin) / (oldRangeMax - oldRangeMin) * (rangeMax - rangeMin) + rangeMin;
    return value * (1024 - 1000) + 1000

def populateList(up, dw, tt):
    arr = [[up, dw, tt], [up, dw, tt]]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = convertBytes(arr[i][j], remap(i))

    return arr

def formatString(up, dw, tt):
    arr = populateList(up, dw, tt)
    res = ''

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = calcPadding(arr[i][j])[0] + arr[i][j] + calcPadding(arr[i][j])[1]

    for el in arr:
        res = res + '|' + el[0] + '|' + el[1] + '|' + el[2] + '|\n'

    return res

f = open('data.json')
content = json.load(f)

today = content['interfaces'][0]['traffic']['days'][0]

date = today['date']

header = '\n|' + calcPadding('Uploaded')[0] + 'Uploaded' + calcPadding('Uploaded')[1]
header = header + '|' + calcPadding('Downloaded')[0] + 'Downloaded' + calcPadding('Downloaded')[1]
header = header + '|' + calcPadding('Total')[0] + 'Total' + calcPadding('Total')[1] + '|\n'

linebreak = '|' + '-' * width + '|' + '-' * width + '|' + '-' * width + '|\n'
values = formatString(today['rx'], today['tx'], today['rx'] + today['tx'])

table = header + linebreak + values

message = '*%(date)s*\n```%(table)s```' % {'date': convertDate(date), 'table': table}