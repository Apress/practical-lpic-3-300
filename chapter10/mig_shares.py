#!/usr/bin/python

import sys
import subprocess

def usage():
	print "Usage: %s SHARES_FILE" % sys.argv[0]
	sys.exit(1)

if len(sys.argv)<2:
	usage()

FILENAME = sys.argv[1]
try:
	fd = open(FILENAME, "r")
	lines = fd.readlines()
	fd.close()
	f2 = open("folders_migrated.txt","w")
except Exception, e:
	print str(e)
	sys.exit(1)

flag = False

for line in lines:
	try:
		if flag:
			if "path" in line:
				indice = line.find("=")
				cmd = "mkdir -p %s" % line[indice+1:]
				try:
					output = subprocess.check_output(cmd,shell=True)
					f2.write(line[indice+1:])
					print "Created %s folder\n" % line[indice+1:]
 				except Exception, e:
					print str(e)
				finally:
					flag = True
		else:

			if line[0]=='[':
				if "[global]" in line:
					pass	
				elif "[homes]" in line:
					pass
				elif "[printers]" in line:
					pass
				elif "[print$]" in line:
					pass
				else:
					flag = True
							
	except Exception,e:
		pass
f2.close()
