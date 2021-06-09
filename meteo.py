
import requests
import json
import csv
from tqdm import tqdm
from requests.api import request
from classes import daycsv, day





def endmonth(month):
    if month == "02":
        return "28"
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12" :
        return "31"
    return "30"



def fetchonLine(date):
    url = "https://api.weather.com/v1/location/RKTN:9:KR/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&startDate=" + date + "&endDate=" + date
    request = requests.get(url)
    data =  json.loads(request.content)

    if request.status_code == 200 and data['metadata']['status_code'] == 200:
        return data['observations'][len(data)//2]


def fetchdata():
    days = []


def processcsv(filepath):
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        listdays = []
        for row in tqdm(csv_reader, desc= 'loading csv file'):
            if line_count == 0:
                line_count += 1
            else:
                d = daycsv(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                listdays.append(d)
                line_count += 1
        print(f'Processed {line_count} lines.')
        return listdays

def linkcsvwithaq(filepath):
    days = []
    daycsv = processcsv(filepath)
    for i in tqdm(daycsv, desc="fetching data online"):
        cordate = i.explicitdate()
        x = fetchonLine(cordate)
        if x != None :
            d = day(cordate, i.airqual, x['wspd'], x['wdir'], x['wdir_cardinal'])
            days.append(d)
    return days

def daytojson(day):
    x = {
        'date' : day.date,
        'pm25' : day.airquality.pm25,
        'pm10' : day.airquality.pm10,
        'o3' : day.airquality.o3,
        'no2' : day.airquality.no2,
        'so2' : day.airquality.so2,
        'co' : day.airquality.co,
        'windspeed': day.windspeed,
        'winddir': day.winddir,
        'windapprdir': day.windapprdir
    }
    return json.dumps(x)

def printjson(days, output):
    f = open(output, 'x')
    f.write('{\"days\" :\n')
    for i in days:
        f.write(daytojson(i))
        f.write(',\n')
    f.write(']}')
    f.close()




x = linkcsvwithaq('daegu-air-quality.csv')
printjson(x, "output.json")
