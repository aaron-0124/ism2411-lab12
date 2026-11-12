import csv
from datetime import datetime


# Exercise 1:
# sales.csv is inside the data folder.


# Exercise 2: 
print("Exercise 2: Raw Rows")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)