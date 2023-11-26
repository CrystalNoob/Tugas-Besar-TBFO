
from colorama import Fore, Style

def print_with_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m",end='')