import openpyxl
from pathlib import Path

excelFile = openpyxl.Workbook()

excelSheet =  excelFile.active
excelSheet.title = "firstSheet"

names = ['Hesham', 'Gannah', 'Samar', 'Islam']
firstSheet = excelFile['firstSheet']
for i in range(1, len(names)+1):
    firstSheet.cell(row=i, column=3).value = names[i-1]

excelFile.save(filename = Path.home() / Path('Desktop') / 'Excel.xlsx')