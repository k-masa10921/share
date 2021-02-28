import os,re,sys,json,time
from datetime import datetime,date,timedelta
from shapely.geometry import Polygon,Point
import search 

#3.7からは元々存在する関数
def fromisoformat(str_date):
    dl = re.split("[-T:]",str_date)

    for i in range(len(dl)):
        dl[i] = int(dl[i])

    dt = datetime(dl[0],dl[1],dl[2],dl[3],dl[4],dl[5])

    return dt

#任意idの指定時間の最新のデータを一件（本日）
#（例）hm1 ,hm2 = (09,00,00),(20,30,00)
def data_each_id(num,hm1,hm2):

    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    fromt = datetime(year,month,day,hm1[0],hm1[1],hm1[2])
    fromt = fromt + timedelta(hours=-9)
    fromt = fromt.isoformat()

    tot = datetime(year,month,day,hm2[0],hm2[1],hm2[2])
    tot = tot + timedelta(hours=-9) 
    tot = tot.isoformat()

    body = search.makebody(search.matchquery('id',num),
            search.timequery(fromt,tot))
    body.update({'size':1})
    body.update({'sort':{'date':'desc'}})
    
    data = search.searchlist("test",body,False)
    
    if data['hits']['total']['value'] != 0:
        return data['hits']['hits'][0]['_source']
    else:
        return False


#{"lat":n,"lon":m"}->(n,m)
def geo_to_shell(geo):
    return (geo['lat'],geo['lon'])

#[{"lat":n1,"lon";m1},...]->[(n1,m1),(n2,m2),...]
def geolist_to_shell(geolist):
    ret = []
    for geo in geolist:
        ret.append(geo_to_shell(geo))
    return ret

def make_polygon(geolist):
    geolist = geolist_to_shell(geolist)
    polygon = Polygon(geolist)
   
    return polygon

#lambda = (["lat":nx,"lon":mx], [{"lat":n1,"lon":m1},{...}...])
def is_place(geo,geolist):
    geo = geo.split(',')
    polygon = make_polygon(geolist)
    point = Point(float(geo[0]),float(geo[1]))

    return polygon.contains(point)

#最新の位置が危険エリアにあるかどうかを検索。
def car_position(deviceID):
    safe = 0
    isArea = 1
    noGPS = 2
    noData = 3

    now = datetime.now()
    #現状10分間にしてるが果たして
    diff = 10
    fromt = now + timedelta(minutes=-diff)
    hm1 = [fromt.hour,fromt.minute,fromt.second]
    hm2 = [now.hour,now.minute,fromt.second]

    data = data_each_id(deviceID,hm1,hm2)
        
    #進入禁止場所の保存,取得方法は未定
    with open("Arealist.txt") as f:
        Arealist = json.load(f)
    if data:
        location =data['location']
        date = data['date']
        date = fromisoformat(date) + timedelta(hours=9)
        date = date.isoformat()    
        if location == []:
            #print('ID:%s No GPS data\ndatetime:%s' % (deviceID,date))
            return noGPS,deviceID,date
        else:
            for Area in Arealist:
                if is_place(location,Area['locations']):
                    #print("ID:%s Specified area\nlocation:%s\ndatetime:%s"
                    #        %(deviceID,Area["name"],date))
                    return isArea,deviceID,Area['name'],date
                else:
                    #print("ID:%s \ndatetime:%" %(deviceID,date))
                    return safe,deviceID,date
    else:
        #print("ID:%s No data for %sminutes" % (deviceID,diff))
        return noData,deviceID,diff    

def is_area_stop():
    state = 0
    pretime = 0
    posttime = 0
    while True:
        pret = car_position(1)
        lstate = pret[0]
        if state == 0 and lstate == 1:
            pretime = pret[3]
            state = 1
        elif state == 1 and lstate == 1:
            posttime = pret[3]
            diff = fromisoformat(posttime) - fromisoformat(pretime)
            print("ID:%s\nArea:%s\ndiff:%s\n" %(pret[1],pret[2],diff))
        elif state == 1 and lstate == 0:
            pretime = 0
            posttime = 0
            state = 0
        else:
            pass
        time.sleep(5)

def main():
    is_area_stop()

if __name__ == '__main__':
    main()
