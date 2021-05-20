import os
import pyfiglet
import re

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def is_not_empty(val):
    return val != ''

def big_print(text):
    result = pyfiglet.figlet_format(text, font = "slant")
    print(result)
    
def parse_flags(inp):
    res = re.findall(r'--(\w+)\s(\w+)', inp)
    return dict((x, y) for x, y in res)
