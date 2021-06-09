import json
from classes import day, airqual, analysis

def toint(str):
    if str == None or str == ' ':
        return -1
    return int(str)

def importjson(path):
    f = open(path)
    days = []
    daysdict = json.load(f)
    for i in daysdict['days']:
        aq = airqual(toint(i['pm25']), toint(i['pm10']), toint(i['o3']), toint(i['no2']), toint(i['so2']) ,toint(i['co']))
        j = day(i['date'], aq, toint(i['windspeed']), toint(i['winddir']), i['windapprdir'])
        days.append(j)
    return days

#def instancepp(an, dict):

def listpp(dict, count):
    for i in dict:
        (x, y) = i
        print ("DIR : "+ x + " prop : "+ str(y/count * 100)[:4]+'%')

def actdic(dict, st):
    if (st == None or str == 'CALM'):
        return 0
    for i in range (len(dict)):
        (x, y) = dict[i]
        if x == st:
            y += 1
            dict[i] = (x, y)
            return 1

    print('error when adding to dictionnary: ' + st)
    return 0



def showsstats(an):
    dictcopy = [
        ('N', 0),
        ('NE', 0),
        ('NNE', 0),
        ('ENE', 0), 
        ('E', 0), 
        ('SE', 0), 
        ('SSE', 0),
        ('ESE', 0), 
        ('S', 0), 
        ('SSW', 0), 
        ('WSW', 0),
        ('SW',0),
        ('W',0), 
        ('NW', 0), 
        ('NNW', 0),
        ('WNW', 0),
        ('CALM', 0)
    ]

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg pm25: ' + str(an.pm25avg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.pm25 > an.pm25avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above pm25 average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below pm25 average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg pm10: ' + str(an.pm10avg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.pm10 > an.pm10avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above pm10 average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below pm10 average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg o3: ' + str(an.pm10avg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.o3 > an.o3avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above o3 average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below o3 average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg no2: ' + str(an.so2avg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.no2 > an.no2avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above no2 average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below no2 average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg so2: ' + str(an.so2avg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.so2 > an.so2avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above so2 average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below so2 average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]
    print('\navg co: ' + str(an.coavg))

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.co > an.coavg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    print('when above co average: '+ str(countabove)+ 'days')
    listpp(dictabove, countabove)
    print("\nwhen below co average: " + str(countbelow) + 'days')
    listpp (dictbelow, countbelow)



x = analysis(importjson('output.json'))
showsstats(x)