import csv
import requests
count=0
with open ( "medical.csv" , "r" ) as f :
    reader = csv.reader ( f )
    with open('medical-sample.csv', 'w', newline='') as m:
        writer = csv.writer(m)
        for line in reader :
            print ( line[0] )
            # resp = requests.get('https://caretaro.com/shopdetail/'+ line[0])
            resp = requests.get(line[0])
            print(resp.status_code)
            if (resp.status_code==404):
                count = count + 1
            writer.writerow([resp.status_code])
            print(count)
        # print(resp.status_code)
