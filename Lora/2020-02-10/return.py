#車が帰る2時間前から位置情報を取得。
#車が帰って来た（特定エリア内に入る）時に終了。
#特定の位置(or一番遠い位置)から帰って来るまでにかかった時間を算出?
#指定した時間から直線距離で1km以内に入ったら通知。

import json,schedule,time
from datetime import datetime,date,timedelta
from shapely.geometry import Polygon,Point
from shapely.ops import nearest_points
from pyproj import Geod

import search
import alert
from googledirection import arrival_time
#globalとして基地局の場所を置く(KIT)
with open("home.txt") as f:
     home = json.load(f)


#時間を指定して関数を実行する例
def preret(rtime):
    def job():
        print("test")

    schedule.every().day.at(rtime).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

#目的地を変える場合alertのis_place等を参照
def is_home(geo):
    return alert.is_place(geo,home[0]["locations"])

def nearestpoint(geo):
    polygon=alert.make_polygon(home[0]["locations"]) 
    geo=geo.split(',')
    point=Point(float(geo[0]),float(geo[1]))

    np1,np2=nearest_points(polygon,point) 
    lat1=np1.xy[0][0]
    lon1=np1.xy[1][0]
    lat2=np2.xy[0][0]
    lon2=np2.xy[1][0]
    return [lat1,lon1,lat2,lon2]

def distance(pl):
    g = Geod(ellps='GRS80')
    azimuth,bkw_azimuth,distance =g.inv(pl[1],pl[0],pl[3],pl[2])
    return distance

    
def now_distance(deviceID):
    now = datetime.now()
    #現状10分間のデータを見るが実際はどうかわからない。
    diff = 10
    fromt = now + timedelta(minutes=-diff)

    hm1 = [fromt.hour,fromt.minute,fromt.second]
    hm2 = [now.hour,now.minute,fromt.second]

    data=alert.data_each_id(deviceID,hm1,hm2)
    if data:
        location = data['location']
        date = data['date']
        date = alert.fromisoformat(date) + timedelta(hours=9)
        date = date.isoformat()
        npoint = nearestpoint(location)
        dst = distance(npoint)
        if dst>0:
            #print("ID:%s distance:%sm\ndatetime:%s\n" 
            #        % (deviceID,dst,date))
            #print("----------------------------")
            return False,deviceID,npoint,date
        else:
            return True,deviceID,date
    else:
        pass

#今後より近いガソリンスタンドのみを表示もしくは時間の平均を出す。
#現状ガソスタをあらかじめ定義しているが、googleapiの機能を使って
#周辺何mに位置するガソスタの情報を得て、そこから検索もできる。
def gas_station(src,dst):
    with open("gas-station.txt") as f:
        gasstas = json.load(f)
    time = 360
    gname = ""
    for gassta in gasstas:
        name = gassta["name"]
        glat = str(gassta["location"]["lat"])
        glon = str(gassta["location"]["lon"])
        glocation= glat + ',' + glon
        atime = arrival_time(src,dst,glocation)
        print("%sに寄れば%s＋給油で10分程？" %(name,atime))
        atime = int(atime.split("分")[0])
        if atime < time:
            time = atime
            gname = name
    return time,gname

#現在地との距離をみて、1km以内であれば、nearest_gas_stationを動かし、
#最も近いガソスタのみを表示する関数を作る。

src = "33.903495,130.79826"
dst = "33.892236,130.840128"

print(gas_station(src,dst))
##後々返却時間を入力して↑の関数を動かす時間を定義する。
