from pathlib import Path

from FilesAndFolders import FilesAndFolders

path = Path.home()/"Desktop"
fold = FilesAndFolders()
fold.create_folder("maxBeat")
# path
print(path.exists())