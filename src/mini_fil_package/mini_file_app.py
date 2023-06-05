from pathlib import Path

from FilesAndFolders import FilesAndFolders

option = eval(input("1 --> to use this app\n"))
filed = FilesAndFolders()
path = Path()
new_path = Path()
folder_name = ""
file_name = ""
my_file = Path()
content ={}
# filed.write_into_file(my_file,)

while option == 1:
    choice = eval(input("1 --> to create folder\n"
                        "2 --> to create file\n"
                        "3 --> to write into file\n"
                        "4 --> to read from file\n"))
    match choice:
        case 1:
            folder_name = input("Enter a name for your new folder\n")
            new_path = filed.create_folder(folder_name)
            break
        case 2:
            file_name = input("Enter a new for the new file\n")
            file_type = input("Enter the type of \n ")
            my_file = filed.create_file(new_path, file_name, file_type)
            break
        case 3:
            file_choice = eval(input("1 --> to write into file just created\n"
                                     "2 --> to write into different file \n"))

            header = [input("The header ")]
            print("what will you like to write in your csv file \n")
            number_of_keys = int(input("Enter the number of keys "))
            # number_of_values = int(input("Enter the number of values "))

            for i in range(number_of_keys):
                key = input("Enter the key ")
                for j in range(1):
                    content[key] = input("Enter the value of choice ")

            match file_choice:
                case 1:
                    filed.write_into_file(my_file, header, content)
                    break
                case 2:
                    other_file = Path(input("Enter file path of choice "))
                    filed.write_into_file(other_file, header, content)
                    break
            break
        case 4:
            fourth_choice = eval(input("1 --> to read from file just created and updated \n"
                                       "2 --> to read from different file \n"))
            match fourth_choice:
                case 1:
                    filed.read_file(my_file)
                    break
                case 2:
                    second_Case = Path(input("Enter the file of your choice \n"))
                    filed.read_file()
            break

    print("you got this far")
    option = eval(input("1 --> to use this app"))
print("lets keep trying")
