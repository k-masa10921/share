import urllib.request
import json
import os

api_key = "AIzaSyCfMS_kgL2S9NgsUvLdkb5OivcykW2KXdc"


def getMapDirection(src,dst,waypoint="",filename=False):
    urlpre =  "https://maps.googleapis.com/maps/api/directions/json?"
    urlpost = "origin={0}&destination={1}&waypoints=via:{2}&mode={3}&alternatives={4}&language={5}&units={6}&key={7}"
    mode = "driving"
    alternatives="true"
    lang = "ja"
    ##unitsは不要か？
    units = "metric"
    
    ##departure_timeを使うと交通状況に合わせた時間が出る
    ##しかし、データあたりの値段が上がるので現在指定していない。
    url = urlpre + urlpost.format(
                src,
                dst,
                waypoint,
                mode,
                alternatives,
                lang,
                units,
                api_key)
    try:
        req = urllib.request.Request(url)
        Direction_data = urllib.request.urlopen(req).read()
        json_data =json.loads(Direction_data)
        
        if filename:
            with open(filename,mode="w") as f:
                print(json_data,file = f)
        
        return json_data
    except:
        print("error urlopen or jsonloads ")
        
        return False


def arrival_time(src,dst,waypoint=""):
    data = getMapDirection(src,dst,waypoint)
    
    return data['routes'][0]['legs'][0]['duration']['text']
    

src = "33.903495,130.79826"
dst = "33.892236,130.840128"

#data = getMapDirection(src,dst,filename="direction2.json")

#print(arrival_time(src,dst))
