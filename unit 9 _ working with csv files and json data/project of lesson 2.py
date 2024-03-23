import csv
from pathlib import Path

file = open(Path.home() / Path('Desktop', 'employees.csv'), 'a', newline='')

add = csv.writer(file)
add.writerow(['Hesham', '300', '02/1/2024'])
add.writerow(['Gannah', '400', '06/5/2023'])
add.writerow(['Samar', '800', '22/3/2021'])

file.close()