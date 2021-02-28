import re
import math

data ='1,1,-108,065740,090120,N,3353.4962,E,13049.8942,19.7,27.3,10,14.44,117.14'

#data->list
listdata = data.split(',')


def getDecimalDegree(dbb,sign):
    degree = int(dbb / 100)
    minute = dbb % 100
    if sign == "S" or sign == "W":
        return degree - (minute / 60)
    elif sign == "N" or sign == "E":
        return degree + (minute / 60)

#shaping
def shaping(ldata, key):
    ### date&time -> yyyy-mm-ddTHH:MM:SS
    if key == "datetime":
        if ldata[3] == '' or ldata[4] == '':
            datetime = ''
        else:
            sdate = re.split('(..)' , ldata[4])[1::2]
            stime = re.split('(..)' ,ldata[3])[1::2]
            sdate.reverse()
            datetime = "20" + "-".join(sdate) + "T" + ":".join(stime)

        return datetime

    elif key == "location":
        if '' in ldata[5:9]:
            location = []
        else:
            lat = float(getDecimalDegree(float(ldata[6]),ldata[5]))
            lon = float(getDecimalDegree(float(ldata[8]),ldata[7]))
            location = str(lat) + "," + str(lon)
        return location

'''
doc = {
        "id":ldata[0],
        "RSSI":ldata[2],
        "date":shaping(ldata, "datetime"),
        "location":shaping(ldata, "location"),
        "altitude":ldata[9],
        "height":ldata[10],
        "satellite_num":ldata[11],
        "velocity":ldata[12],
        "direction":ldata[13]
        }
'''
#print(shaping(listdata,"datetime"))
#print(shaping(listdata,"location"))


