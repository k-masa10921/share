import os
import sys
import elasticsearch
import datashaping as shape

es = elasticsearch.Elasticsearch("10.3.10.123:9200")

static = {
        "mappings" : {
            "properties" :{
                "id"            : {"type" : "short"},
                "date"          : {"type" : "date",
                    "format" : "date_hour_minute_second"},
                "location"      : {"type" : "geo_point"},
                "altitude"      : {"type" : "float"},   
                "height"        : {"type" : "float"},
                "satellite_num" : {"type" : "short"},
                "velocity"      : {"type" : "float"},
                "direction"     : {"type" : "float"}
                }
            }
        }

dynamic = {
        "mappings" : {
            "properties" :{
                "id"            : {"type" : "short"},
                "RSSI"          : {"type" : "short"},
                "date"          : {"type" : "date",
                    "format" : "date_hour_minute_second"},
                "location"      : {"type" : "geo_point"},
                "altitude"      : {"type" : "float"},   
                "height"        : {"type" : "float"},
                "satellite_num" : {"type" : "short"},
                "velocity"      : {"type" : "float"},
                "direction"     : {"type" : "float"}
                }
            }
        }

###ldataの個数による場合わけが必要か。
###RSSI値がgeoipと異なるパターンのデータ入力を考えるべき
def makedoc(data):
    ldata = data.split(',')
    if len(ldata) == 14:
        doc = {
                "id":ldata[0],
                "RSSI":ldata[2],
                "date":shape.shaping(ldata, "datetime"),
                "location":shape.shaping(ldata, "location"),
                "altitude":ldata[9],
                "height":ldata[10],
                "satellite_num":ldata[11],
                "velocity":ldata[12],
                "direction":ldata[13]
                }
        return doc

    elif len(ldata) == 12:
        ldata.insert(1,"0")
        ldata.insert(2,"-0")
        doc = {
                "id":ldata[0],
                "date":shape.shaping(ldata, "datetime"),
                "location":shape.shaping(ldata, "location"),
                "altitude":ldata[9],
                "height":ldata[10],
                "satellite_num":ldata[11],
                "velocity":ldata[12],
                "direction":ldata[13]
                }
        return doc
    
    else:
        print("datasize is wrong")


def indexdelete(name="test"):
    if es.indices.exists(index = name):
        if es.indices.exists(index = name):
            print("%s cannot be deleted" % name)
            print(res['result'])
        else:
            print("Removed %s" % name)
    else:
        print("%s does not exist" % name)


def indexmake(indexname="test",mappingname=dynamic):
    es.indices.create(index = indexname,body = mappingname)
    print("Made index %s" % indexname)


def senddata(doc,indexname="test",typename="_doc"):
    res = es.index(index = indexname, doc_type = typename, body = doc)


###readlinesでいったん読み出しすることで時間食ってそう
def sendfile(path,indexname="test",typename="_doc"):
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        line =line.strip()
        if line != '':
            senddata(makedoc(line),indexname,typename)
                
    print("Send %s\nindex=%s\ntype=%s" % (path,indexname,typename))


#indexdelete()
#indexmake()
#sendfile("SF12carfr20111.txt")

###適当に作っただけだからもっと設計すべき
def main():
    argvs = sys.argv
    argc = len(argvs)
    text = "%s -D [index]\n%s -M [index,mapping]\n%s filename [index,type]" % (argvs[0],argvs[0],argvs[0])
    if (argc <= 1):
        print(text)

    else:
        if argvs[1] == '-D':
            if argc == 2:
                indexdelete()
            else:
                indexdelete(argvs[2])
        elif argvs[1] == '-M':
            if argc == 2:
                indexmake()
            elif argc ==3:
                indexmake(argvs[2])
            else:
                indexmake(argvs[2],argvs[3])
        else:
            if argc == 2:
                sendfile("%s/%s" % (os.getcwd(),argvs[1]))
            else:
                sendfile("%s/%s" % (os.getcwd(),argvs[1]),argvs[2],argvs[3])

if __name__ == '__main__':
    main()
