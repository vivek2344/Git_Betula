import os
import sys
import subprocess
import time
import pexpect
from pexpect import popen_spawn

from subprocess import Popen, PIPE

cmd = 'C:/cygwin64/home/BGH48937/Betula_Client'

#Instantiate the Betula Client App
child = pexpect.popen_spawn.PopenSpawn('Betula_Client.exe', cwd=os.path.dirname(cmd))

#Redirect the child console logs to a text file
fout = open('my_log.txt','w')
child.logfile = fout

#Print the child console
#child.logfile_read = sys.stdout
child.expect('Stop reconnect')

# Device Settings option
child.sendline('2')
child.expect ('Allow Device.')
arraylist = {}
index = {}
#print child.before
child.expect('Disconnect All')

#Request discovery
child.sendline('1')
child.expect(['Start Read Device ID.', 'Remind Note 3'])
print 'Found a match'
child.sendline('2')
child.expect('CreateBond.')
with open("my_log.txt") as f:
	for line in f:
		if "Mi A1" in line:
			arraylist = {}
			arraylist = line.split()
			index = arraylist[0]
index = str(arraylist[0])
print index
print 'Sending command 4'
child.sendline('4')
child.expect('Select device:')
child.sendline(index)
child.expect('Pairing progress:')
#delay of 5sec
time.sleep(5)
child.sendline('10')
child.expect('Accept pairing [Y/N]')
child.sendline('Y')
child.expect('Allow Device')
#print child.before
def LastNLines(f,n):
	with open(f) as file:
		print('Last ',n,' lines from file: ' ,f)
		for line in (file.readlines() [-n:]):
			print line
name='my_log.txt'
n=1
try:
	LastNLines(name,n)
except:
	print('File error...')
	
"""

	
#child.expect('Pairing progress:')
#print child.before
#child.sendline('10')
#child.expect('Allow Device')
#print child.before
#child.sendline('Y')
#print child.before
"""
