import os
import sys

user_directory = "E:\\Python_projects\\os_projects\\1.Simple_file_lister"  # input("Enter the path of the directory: ")

directory_list = []
file_list = []
directory_dict = {}

try:
    for dirpath, dirnames, filenames in os.walk(user_directory):
        directory_dict[dirpath] = filenames


except FileNotFoundError:
    print("Directory Not Found")
    sys.exit(1)
except PermissionError:
    print("Permission Denied")
    sys.exit(1)
