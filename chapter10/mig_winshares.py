#!/usr/bin/python

import sys
import subprocess

def usage():
        print "Usage: %s FILE" % sys.argv[0]

if len(sys.argv)<2:
        usage()
        sys.exit(1)

FILE = sys.argv[1]
OUTPUT_FILE = "add_to_smb.conf"


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

fd2 = open(OUTPUT_FILE, "w")

for line in lines:
        if (flag==1):
                if bottom in line:
                        flag = 0
                else:
			if line.find("$")<0:
				share_name = line[:line.find(" ")]
				linea = "[" + share_name +']\n'
				try:
					fd2.write(linea)
					ruta = "/samba/" + share_name
					cmd = "mkdir -p " + ruta
					print "Creating %s" % share_name
					output = subprocess.check_output(cmd, shell=True)
					print output
					fd2.write('\t')
					fd2.write('path = ')
					fd2.write(ruta)
					fd2.write('\n')
					fd2.write('\tread only = Yes\n')
					fd2.write('\tguest ok = No\n')
				except Exception, e:
					print str(e)
				
        else:
                if top in line:
                        flag = 1
fd2.close()
