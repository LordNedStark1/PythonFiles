from pathlib import Path
#
# path = Path(r"\root\media\private\me.jpeg")
# print (path)
# path2 = path.home()
# path3 = path.cwd()
# print(path2)
# print (path3)


# from pathlib import Path
# import shutil
# path = Path.cwd()/"new_directory"/"dir_2"/"ridwan.txt"
# #
# path.touch()
# # destination = Path.cwd()/"new_directory2"/"ridwan.txt"
# # path.replace(destination)
#
# # new_path = Path.cwd()/"new_directory3"
# # new_path.rmdir()
#
# path_next = Path.cwd()/"new_directory2"
# if path_next.exists():
#     shutil.rmtree(path_next)

path = Path.cwd()/"new_directory"/ "lovestory.txt"

numbers =[
        [29, 43, 54, 65, 56],
        [23, 45, 66, 65, 67],
        [33, 43, 43, 34, 23],
        [67, 87, 56, 65, 65],
        ]

with open(path, encoding= "utf-8", mode= "w") as file:
    for number in numbers:
        file.write(str(number[0]))
        for num in number[1:]:
            file.write(f",{num}")
        file.write('\n')


# with open(path, encoding= "utf-8", mode= "r") as file:
#     # print(file.read())
#     lint = file.read()
#     lint_next = lint.split()
#     list_one =[]
#     list_two = []
#     list_three=[]
#     list_four=[]
#     combine = []
#     list_one =f"[{lint_next[0]} ]"
#     list_two = f"[{lint_next[1]} ]"
#     list_three = f"[{lint_next[2]} ]"
#     list_four = f"[{lint_next[3]} ]"
#     combine.append( list_one)
#     combine.append( list_two)
#     combine.append(list_three)
#     combine.append(list_four)
#     # print(numbers)
#     # print (combine)
#
# print("this is  numbers\n")
# for i in numbers:
#     print(i)
#
# print("\n")
# print("this is combine \n")
#
# for i in combine:
#     print(i)
corrections =[]

# def decode(string):
#     list = string.split(",")
#     corrections.append([int(num)for num in list])



with open(path, encoding="utf-8", mode="r") as file:
    lines = file.readline()

    # for line in lines:

        # decode(line)

# print(corrections)

correct = []

def decode (list):
    list_one = list.split(",")
    correct.append([int(num) for num in list_one])

with open(path, encoding="utf-8", mode="r") as file:
    links = file.readlines()
    for link in links:
        decode(link)

print (correct == numbers)

# correcton.append(decode())
    # print([int(num)for num in x])

    # for i in range(len(file.readlines())):
    #     print (file.readline())

    # print("[")
    # print("[", file.readlines()[1]," ]")
    # print("[", file.readlines()[0]," ]")
    # # print("[", file.readlines()[2]," ]")
    # # print("[", file.readlines()[3]," ]")
    # print(" ]")
# path.touch()

# file = path.open(mode="w", encoding= "utf-8")
# mass = "i love u soo much and can't stop loving u"
# file.write( mass)
# print(file)
# with path.open(mode="w", encoding= "utf-8") as file:
#     file.write("holle kemi,\n")
#     file.write("I really miss you. I will join in the next class\n")


# with path.open(mode="r+", encoding= "utf-8") as file:
#     print(file.read())
#     file.write("holle kemi,\n")
#     file.write("I really miss you. I will join in the next class\n")


# with path.(mode="a+", encoding= "utf-8") as file:
#     # file.write("holle kemi,\n")
#     # file.write("I really miss you. I will join in the next class\n")
#     print(file.read())
#     file.write("master plus")
#     print(file.read())

# with path.open(mode="r", encoding= "utf-8") as file:
#     # print(file.read())
#     # print(file.readline())
#
#     print(file.readlines()[1])

# with open(path, mode="r", encoding= "utf-8") as file:


# mass = "i love u soo much and can't stop loving u"
# file.write( mass)
# print(file)