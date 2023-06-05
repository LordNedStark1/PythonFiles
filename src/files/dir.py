from pathlib import Path

# cwd = Path.cwd()
#
# dir = [
#     Path.cwd()/ "new_directory1",
#     Path.cwd()/ "new_directory2",
#     Path.cwd()/ "new_directory3",
#     Path.cwd()/ "new_directory4"
#     ]
#
# for path in dir:
#     path.mkdir(exist_ok=True)

# for dir in cwd.iterdir():
#     print(dir)

# for dir in cwd.glob("*\**"):
#     print(dir)

# for dir in cwd.glob("*.py"):
#     print(dir)
# for dir in cwd.rglob("*.txt"):
#     print(dir)
# for dir in cwd.rglob("*.txt"):
#     print(dir)
#
# for dir in cwd.rglob("*"):
#     print(dir)

# for dir in cwd.rglob("new_directory[1234]"):
#     print(dir)

source = Path.cwd()/"new_directory"/ "dir_2"
print(source.exists())
destination = Path.cwd()
print(destination)
# / "new_directory1"/"unknownnn.txt"
# source.replace(destination)
# source = Path("C:/Users/USER/Desktop/my_folder/my_file.txt")
# print(source.exists())
# destination = Path("C:/Users/USER/Desktop/next_folder")
# source.replace(destination)