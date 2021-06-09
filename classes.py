class daycsv:
    def __init__(self, date, pm25, pm10, o3, no2, so2, co):
        self.date = date
        self.airqual = airqual(pm25, pm10, o3, no2, so2, co)

    def explicitdate(self):
        datearr = self.date.split('/')

        if len(datearr[1]) == 1 :
            datearr[1] = '0'+ datearr[1]
        if len(datearr[2]) == 1 :
            datearr[2] = '0'+ datearr[2]
        return datearr[0] + datearr[1] + datearr[2]
    

class analysis:
    def __init__(self, days):
        self.days = days
        self.pm25avg = self.setpm25avg()
        self.pm10avg = self.setpm10avg()
        self.o3avg = self.seto3avg()
        self.no2avg = self.setno2avg()
        self.so2avg = self.setso2avg()
        self.coavg = self.setcoavg()

    def setpm25avg(self):
        pm25avg = 0
        for i in self.days:
            pm25avg += i.airquality.pm25
        pm25avg = pm25avg/len(self.days)
        return pm25avg


    def setpm10avg(self):
        pm10avg = 0
        for i in self.days:
            pm10avg += i.airquality.o3
        pm10avg = pm10avg/len(self.days)
        return pm10avg

    def seto3avg(self):
        o3avg = 0
        for i in self.days:
            o3avg += i.airquality.o3
        o3avg = o3avg/len(self.days)
        return o3avg

    def setno2avg(self):
        no2avg = 0
        for i in self.days:
            no2avg += i.airquality.no2
        no2avg = no2avg/len(self.days)
        return no2avg

    def setso2avg(self):
        so2avg = 0
        for i in self.days:
            so2avg += i.airquality.so2
        so2avg = so2avg/len(self.days)
        return so2avg
    
    def setcoavg(self):
        coavg = 0
        for i in self.days:
            coavg += i.airquality.co
        coavg = coavg/len(self.days)
        return coavg

class airqual:
    def __init__(self, pm25, pm10, o3, no2, so2, co):
        self.pm25 = pm25
        self.pm10 = pm10
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.co = co



class day:
    def __init__(self, date, airquality, windspeed, winddir, windapprdir):
        self.date = date
        self.airquality = airquality
        self.windspeed = windspeed
        self.winddir = winddir
        self.windapprdir = windapprdir

