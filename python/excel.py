import xlrd
import openpyxl

# get excelfile
# 1 2 3
# 4 5 6
wb = openpyxl.load_workbook("test.xlsx")
print(type(wb))
print(wb.sheetnames)


# get sheet=test
sheet = wb["test"]
print(type(sheet))

# get cell
cell = sheet["A1"]
print(type(cell))
print(cell.value)

cell = sheet.cell(row=1, column=1)
print(cell.value)
