from pathlib import Path
import csv

from FilesAndFolders import FilesAndFolders

path = Path.cwd()/"new_directory"/ "consensus.csv"

path.touch()
# # path1 = Path.cwd()
# # print(path1)
# # path2 = Path.home()/"PycharmProjects"/"pythonfilesJonathan"/"src"/"Animal"/"Pig.py"/"man.py"
# # path2.touch()
# # print (path2.exists())
# # print(path2)
# numbers =[
#     [23, 32, 54, 54, 65],
#     [87, 54, 56, 56, 67],
#     [56, 76, 45, 76, 54]
# ]
# with open(path, encoding= "utf-8", mode= "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)
#
# with open(path, encoding="utf-8", mode="r") as file:
#     reader = csv.reader(file)
#     for this in reader:
#         if len(this)!= 0:
#             print(this)
census = [
    {
        "name": "Ned",
        "isSingle": False,
        "cohort":  15,
        "status": "COMPLICATED"
    },
    {
        "name": "Rid-wan",
        "cohort": 15,
        "isSingle":True,
        "status": "UNKNOWN"
    },
    {
      "name": "Timmy",
        "isSingle": True,
        "cohort":  15,
        "home": "far",
        "status": "UnDISCLOSED"
    }
]
fieldnames = ["name", "isSingle","cohort", "status", "home"]

file_test = FilesAndFolders()


file_test.write_into_file(path, fieldnames, census)



path2= Path.cwd()/"dir.py"
print(path2.exists())

with open(path2, encoding="utf-8", mode="r") as file:
    lines = file.readlines()
    print(lines)


# with open(path, encoding= "utf-8",mode="r+" )as file:
#     writer = csv.DictWriter(file,
#         fieldnames = ["name", "isSingle","cohort", "status", "home"])
#     writer.writeheader()
#     writer.writerows(census)