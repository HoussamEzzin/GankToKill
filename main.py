import argparse
import paramiko
import socket
import os
from bruteForce import brute_force_ssh
from portScanner import port_scanner

def main(attack_type):
    if attack_type == 'brute_ssh' :
        target_ip = input('Target IP : ')
        users_file = input('Users file (with extension) : ')
        passwords_file = input('Passwords file (with extension) : ')
        brute_force_ssh(target_ip,users_file,passwords_file)
    elif attack_type == 'scan' :
        target_ip = input('Target IP : ')
        ports = input('Ports : ')
        ports = ports.split(' ')
        port_scanner(target_ip,ports)
        
	



if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="python main.py ATTACKTYPE HOST USERSFILE PASSWORDSFILE")
    parser.add_argument('attack_type',type=str,metavar='ATTACKTYPE', help='determine the chosen attack')
  

    args = parser.parse_args()
    main(args.attack_type)