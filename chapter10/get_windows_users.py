#!/usr/bin/python

import sys
import subprocess

def usage():
        print "Usage: %s FILE" % sys.argv[0]

if len(sys.argv)<2:
        usage()
        sys.exit(1)

FILE = sys.argv[1]

try:
        fd = open(FILE, "r")
        lines = fd.readlines()
        fd.close()
except Exception,e:
        print str(e)
        sys.exit(2)

top = '---------'
bottom = 'The command completed successfully'
flag = 0
users = []

for line in lines:
        if (flag==1):
                if bottom in line:
                        flag = 0
                else:
                        users.append(line.split())
        else:
                if top in line:
                        flag = 1

for user in users:
        for element in user:
                try:
                        print "Creating Linux user %s" % element
                        cmd = "useradd -m " + element                        
                        output = subprocess.check_output(cmd, shell=True)
                        print output
                        print "Creating Samba user %s" % element
                        cmd = "smbpasswd -a -n " + element                        
                        output = subprocess.check_output(cmd, shell=True)
                        print output

                except Exception ,e:
                        print(str(e))
                        sys.exit(3)
