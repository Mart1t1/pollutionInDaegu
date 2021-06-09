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

def quicksummary(dictabove, dictbelow, count, type):
    #we consider that the wind comes from China if it comes from
    #North to South South West
    dirs = ['N', 'NW', 'NWN', 'NNW', 'W', 'SW', 'SSW', 'WSW']
    print('\nbased on the studies on '+ str(count)+ ' days, we can say that, regarding '+ type)

    fromChina = 0

    for i in dictabove:
        (x, y) = i
        if x in dirs:
            fromChina +=y
    
    print("when days are more polluted than average, wind comes from China "+ str(fromChina/count * 100)[:4]+'% of the times')

    fromChina = 0
    for i in dictbelow:
        (x, y) = i
        if x in dirs:
            fromChina +=y
    
    print("when days are less polluted than average, wind comes from China "+ str(fromChina/count * 100)[:4]+'% of the times')



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

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.pm25 > an.pm25avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'pm25')

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.pm10 > an.pm10avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'pm10')

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.o3 > an.o3avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'o3')

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.no2 > an.no2avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'no2')

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.so2 > an.so2avg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'so2')

    dictabove = dictcopy[:]
    dictbelow = dictcopy[:]

    countabove = 0
    countbelow = 0
    for i in an.days:
        if i.airquality.co > an.coavg:
            countabove += actdic(dictabove ,i.windapprdir) 
        else:
            countbelow += actdic(dictbelow, i.windapprdir)
    quicksummary(dictabove, dictbelow, countabove+countbelow, 'co')

    

x = analysis(importjson('output.json'))
showsstats(x)