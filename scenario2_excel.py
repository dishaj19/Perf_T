import openpyxl
from openpyxl import workbook, load_workbook

book = load_workbook('scenario2ID1111.xlsx')
sheet = book.active
print(sheet['A1'].value)







