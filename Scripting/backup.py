'''
Created on Jan 10, 2019

@author: Krishnakanth M
'''
import subprocess
import sys


try:
    subprocess.check_output('cd /opt/genkins', shell=True)
except subprocess.CalledProcessError:
    print("Unexpected error:", sys.exc_info()[0])

try:
    global comms
    comms = ['tar -cvf  /var/temp/backup/backup.tar /opt/genkins/*', 'scp [options] username1@source_host:directory1/filename1 username2@destination_host:directory2/filename2'];
    
    subprocess.call(comms[0],shell=True);
except:
    print("File corrupt")

try:
    subprocess.call(comms[1],shell=True);
except:
    pass