from pathlib import Path

path = Path.cwd()/"see_fifteen"/"elitee.txt"
# if not path.exists():
#     path.mkdir()
# path.mkdir(exist_ok=True)
# path.touch()

# print(path.is_file())

# path1 = Path.cwd()/"new_directory"/ "dir_1"
path2 = Path.cwd()/"new_directory"/ "dir_2"/ "unknownnn.txt"
path2.mkdir(exist_ok=True)
# path1.mkdir(exist_ok=True, parents=True )
# path2.touch()
# path2.unlink()
path2 = Path.cwd()
print(path2)
