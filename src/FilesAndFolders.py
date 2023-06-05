from pathlib import Path
import csv


def delete_file(file: Path):
    if file.exists():
        file.unlink()
    else:
        print("file does not exist")


def delete_folder(folder: Path):
    if folder.exists():
        if folder.is_empty():
            folder.rmdir()
        else:
            option = eval(input("folder is not empty\n"
                                "1--> to delete anyway\n"
                                "2--> to  exit"))
            match option:
                case 1:
                    folder.rmdir()
                case 2:
                    quit()
    else:
        print("folder does not exist")


class FilesAndFolders:

    def __init__(self):
        self._id = 2
        self._folder = None
        self._path = Path.home() / "Desktop"
        self._my_list = []

    def create_folder(self, location: str):
        new_path = self._path/ "Folder-Created"
        new_path.mkdir(exist_ok= True)
        make_folder = new_path / "Folder-Created" / location

        if not make_folder.exists():
            make_folder.mkdir(exist_ok= True)
            print("Folder created ", make_folder)
            return make_folder
        else:
            option = eval(input("folder already exists.\n"
                                "--> 1 to create a new different folder\n"
                                "--> 2 to override existing folder\n"
                                "--> 3 to abort completely"))
            match option:
                case 1:
                    folder_path = location + str(self._id)
                    make_other_folder = new_path / folder_path
                    make_other_folder.mkdir()
                    self._my_list = make_other_folder
                    self._id += 1
                    print("folder created ", make_other_folder)
                    return make_other_folder
                case 2:
                    make_folder.rmdir()
                    make_folder.mkdir()
                    self._my_list = make_folder
                case 3:
                    quit()

    def create_file(self, folder_path: Path, file_name, file_type):
        new_path = folder_path
        concated = file_name + file_type
        make_file = new_path / concated

        if not new_path.exists():
            make_file.touch()
            print("file created ", make_file)
            return make_file
        else:
            option = eval(input(f"{folder_path}, {file_name}, {file_type} file already exists.\n"
                                "--> 1 to create a new different file\n"
                                "--> 2 to override existing file\n"
                                "--> 3 to abort completely"))
            match option:
                case 1:
                    file_path = file_name + str(self._id) + file_type
                    make_other_file = new_path / file_path
                    make_other_file.touch()
                    self._my_list = make_other_file
                    print("file created ", file_path,"\n", make_other_file)
                    return make_other_file
                case 2:
                    make_file.unlink()
                    make_file.touch()
                    self._my_list = make_file
                case 3:
                    quit()

    def view_folder(self, folder_location: Path):
        pass

    def view_all_folders_in(self, folder_location: Path):
        pass

    def read_file(self, path_to_find: Path):
        with open(path_to_find, encoding="utf-8", mode="r") as file:
            lines = file.readlines()
            print(lines)

    def write_into_file(self, path_to_find: Path, header: list, file_to_write):
        with open(path_to_find, encoding="utf-8", mode="w") as file:
            writer = csv.DictWriter(file,
                                    fieldnames= header)
            writer.writeheader()
            writer.writerows(file_to_write)


# path = Path.cwd()
# folder = FilesAndFolders()
# folder.creat_file(path, "head", ".txt")
# delete_file(path / "head2.txt")
