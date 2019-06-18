#!/usr/bin/python

import subprocess
import sys

def usage():
        print "Usage: %s USERS_FILE" % sys.argv[0]
        sys.exit(1)

if len(sys.argv)<2:
        usage()

FILENAME = sys.argv[1]
try:
        fd = open(FILENAME, "r")
        lines = fd.readlines()
        fd.close()
except Exception, e:
        print str(e)
        sys.exit(2)

for line in lines:
        try:
                print "Creating Linux user %s" % line.split(":")[0]
                cmd = "useradd -m -c '" + line.split(":")[2].strip() + "' " + line.split(":")[0]
                output = subprocess.check_output(cmd, shell=True)
                print output
                print "Creating Samba user %s" % line.split(":")[0]
                cmd = "smbpasswd -a -n " +  line.split(":")[0]
                output = subprocess.check_output(cmd, shell=True)
                print output

        except Exception,e:
                print str(e)

