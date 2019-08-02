import os
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
os.system('resize -s 24 80 > /dev/null')
#-----------------------------------------------------
def check():
	exst = str(os.path.exists('.agrmnt.txt'))
	if exst == "True":
		f = open(".agrmnt.txt","r")
		if f.mode =="r":
			contents = f.read()
			if contents[0] == "y" or contents[0] == "Y" or contents[0:3] == "yes" or contents[0:3] == "YES":
				os.system('python3 ezzz_tool.py')
			elif contents[0] == "n" or contents[0] == "N" or contents[0:3] == "no" or contents[0:3] == "NO":
				print("You need to accept agreement first to use the tool.")
				os.system('rm -r .agrmnt.txt')
		f.close()
	else:
		accept = input("\nEzzz tool is only for testing, education purposes and can only be used where strict consent has been given. Any coincidence because of using this tool represents only and only result of your actions. The author does not hold any responsibility for the illegal/unethical use of this tool. Do you accept this agreement? (Y/N) : ")
		if accept != "y" and accept != "Y" and accept != "yes" and accept != "YES" and accept != "n" and accept != "N" and accept != "no" and accept != "NO":
			check()
		else:
			a = "touch .agrmnt.txt | echo "+accept+" > .agrmnt.txt"
			os.system(a)
			check()
check()