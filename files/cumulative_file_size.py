# Python code​​​​​​‌​‌‌​‌​​‌​‌​​​‌‌‌‌‌​​​​‌‌ below
# Use print("messages...") to debug your solution.

import os
from os import path

show_expected_result = False
show_hints = False


def file_info():
    result = 0
    dir = path.curdir
    print(dir)
    if path.exists(dir) and path.isdir(dir):
        print("deps exists and is dir", dir)
        for file in os.listdir(dir):
            file = dir + "/" + file
            print(path.isfile(file))
            if file.endswith(".txt") and path.isfile(file):
                result += path.getsize(file)

    return result


print(file_info())