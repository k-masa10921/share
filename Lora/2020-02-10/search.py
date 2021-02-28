import elasticsearch
import json
#ex
import elasticprocess as process

es = process.es


#検索した結果を返す、検索条件はbody
def searchlist(index,body,printflag=True):
    res = es.search(index = index,body = body)
    if printflag:
        print("Got %d Hits" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print(hit["_source"])
    return res

#Change '2019-01-09' to '2019-01-09T00:00:00'
def timequery(fromtime,totime,flag=True):
    def aux(time):
        if len(time.split('T')) == 1:
            return time + 'T00:00:00'
        else:
            return time
    
    fromtime=aux(fromtime)
    totime=aux(totime)
    body = {'range':{'date':{'from':fromtime,'to':totime}}}
    
    return body


#Make geo_polygon query, [{"lat":33.512512,"lon":130.412424},...]
def geoquery(geolist):
    body = {'geo_polygon':{'location':{}}}
    body['geo_polygon']['location'].update({'points':geolist})
    
    return body


#Make query to search for matching data.
def matchquery(field,data):
    body = {'match':{}}
    body['match'].update({field:data})

    return body

#Make body required for search
def makebody(*args):
    query = [{'match_all': {}}] 
    body = {'size':10000,'query':{'bool':{}}}

    if len(args) >= 1:
        for arg in args:
            query.append(args)

    body['query']['bool'].update({'must': query})
    
    return body    
