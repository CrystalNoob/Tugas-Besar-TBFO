
from colorama import Fore, Style

def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m",end='')

def isSubArray(arr1,arr2):
    is_sub = True

    if (len(arr1) > len(arr2)):
        return False
    for i in range(len(arr1)):
        if (arr1[i] not in arr2):
            return False
    return True
            

