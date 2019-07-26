"""
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.PURPLE+color.BOLD+"purple")
print(color.CYAN+color.BOLD+"cyan")
print(color.DARKCYAN+color.BOLD+"darkcyan")
print(color.BLUE+color.BOLD+"blue")
print(color.GREEN+color.BOLD+"green")
print(color.YELLOW+color.BOLD+"yellow")
print(color.RED+color.BOLD+"red")
print(color.UNDERLINE+color.BOLD+"underline"+color.END)
"""

#import os
#temp = "ls"
#a = os.system(temp)
temp = input("Hello")
print(ord(temp))
#if temp == "\r"
	#print("ZZZ")
