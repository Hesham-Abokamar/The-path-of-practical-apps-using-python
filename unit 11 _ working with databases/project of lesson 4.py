import sqlite3
import openpyxl
from pathlib import Path

connection = sqlite3.connect(str(Path.home() / Path("Desktop", "DataBase.db")))
cursor = connection.Cursor()
cursor.execute("SELECT * FROM students")
data = cursor.fetchall()
connection.close()

excel_sheet = openpyxl.Workbook()
active_sheet = excel_sheet.active

column_names = [description[0] for description in cursor.description]
active_sheet.append(column_names)

for row in data:
    active_sheet.append(row)

excel_file_path = str(Path.home() / Path("Desktop", "project.xlsx"))
excel_sheet.save(excel_file_path)