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

flag = 0
groups = []

for line in lines:
        if (line.find("User name")>-1):
		USER = line[9:].strip()
		flag = 1
	if (flag==1):
		if (line.find("Local Group Memberships")>-1):
			while (line.find("*")>-1):
				line2 = line[line.find("*")+1:]
				group = line2[:line2.find(" ")]
				groups.append(group)
				line = line2[line2.find(" "):]
				line = line2
				try:
					print "Creating group %s if it does not exists" % group
					cmd = "groupadd " + group
					output = subprocess.check_output(cmd, shell=True)
					print output
				except Exception, e:
					print(str(e))
			lista = ""
			for grupo in groups:
				lista = lista + grupo + ","
			lista = lista[0:len(lista)-1]
			try:
				print "Adding user %s to the groups" % USER
				cmd = "usermod -G " + lista + " " + USER
				output = subprocess.check_output(cmd, shell=True)
				print output
			except Exception, e:
				print(str(e))
			
			flag = 0
			groups = []
