import os
import sys

user_directory = input("Enter the path of the directory: ")

directory_list = []
file_list = []
directory_dict = {}

try:
    for dirpath, dirnames, filenames in os.walk(user_directory):
        print(dirnames)
        # directory_list.append(dirnames)
        # file_list.append(filenames)
        directory_dict[tuple(dirnames)] = tuple(filenames)
    # print(directory_list)
    # print(file_list)
    # print(directory_dict)


except FileNotFoundError:
    print("Directory Not Found")
    sys.exit(1)
except PermissionError:
    print("Permission Denied")
    sys.exit(1)
