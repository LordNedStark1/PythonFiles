from pathlib import Path
import csv

# from files.excel_sheet import writer

path = Path.cwd() / "my_documentation.csv"
if not path.exists():
    path.touch()

count = int(input("How many time to you want to input "))

my_dct = {}
my_list = []

for i in range(count):
    key = input("enter a key ")
    for j in range(1):
        value = input("enter a value ")
        my_dct[key] = value

my_list = [my_dct]

with open(path, encoding="utf-8", mode="r+") as file:
    writer = csv.DictWriter(file, fieldnames=["man", "woman", "child", "lover"])
    writer.writeheader()
    writer.writerows(my_list)

print(my_dct)
