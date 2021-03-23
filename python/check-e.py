import openpyxl
import requests
import csv
import sys
path = "C:/Users/k_mas/Desktop/"
name = input()
wb = openpyxl.load_workbook(path+name+"_xml用URL.xlsx")
print(wb.sheetnames)
# sheet = wb.worksheets[0]
# cell = sheet["A1"]
# print(cell.value)
for sheet in wb:
    for row in sheet.rows:
        addrs = []
        for cell in row:
            addrs.append(cell.value)
            # print(addrs)
            for link in addrs:
                print(link)
                try:
                    resp = requests.get(link, timeout=(15))
                    print(resp.status_code)
                    if(resp.status_code == 200):
                        print("ok")
                        if(wb.index(sheet) == 0):
                            with open(name+'_ トップ.csv', 'a', newline='') as m:
                                writer = csv.writer(m)
                                writer.writerow([link])
                        if(wb.index(sheet) == 1):
                            with open(name+'_カテゴリ.csv', 'a', newline='') as m:
                                writer = csv.writer(m)
                                writer.writerow([link])
                        if(wb.index(sheet) == 2):
                            with open(name+'_独自ページ.csv', 'a', newline='') as m:
                                writer = csv.writer(m)
                                writer.writerow([link])
                        if(wb.index(sheet) == 3):
                            with open(name+'_商品詳細.csv', 'a', newline='') as m:
                                writer = csv.writer(m)
                                writer.writerow([link])
                except requests.exceptions.Timeout as error:
                    print("timeout")
                    with open(name+'_ timeout.csv', 'a', newline='') as m:
                        writer = csv.writer(m)
                        writer.writerow([link])
                    continue
