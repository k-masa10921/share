import requests
import csv
count=0
with open('ver2.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        link = ("https://iryoking.com/shopdetail/"+row[0])
        resp = requests.get(link)
        print(resp.status_code)
        if(resp.status_code == 200):
            print("ok")
            with open('result.csv','a',newline='') as m:
                writer = csv.writer(m)
                writer.writerow([link])
        elif(resp.status_code == 404):
            count = count + 1
        print(count)
