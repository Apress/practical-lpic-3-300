#!/usr/bin/python

import datetime
import sys
import datetime

def usage():
        print "Usage: %s number_of_users" % sys.argv[0]

def main():
        if len(sys.argv)<2:
                usage()
                sys.exit(1)
        nusers = int(sys.argv[1])
        print "Generating LDIF file for %d users..." % nusers
        fd = open("users.ldif", "w")
        for i in range(1, nusers+1):
                print "Generating user %d..." % i
                ahora = datetime.datetime.now()
                nombre = "dummy" + str(ahora.year) + str(ahora.month) + str(ahora.day) + str(ahora.hour) + str(ahora.minute) + str(ahora.second) + str(ahora.microsecond)
                linea = "dn: cn=%s,ou=users,dc=linuxaholics,dc=com" % nombre
                fd.write(linea)
                fd.write('\n')
                linea2 = "cn: %s" % nombre
                fd.write(linea2)
                fd.write('\n')
                fd.write('sn: dummys\n')
                fd.write('objectClass: inetOrgPerson\n')
                linea4 = "userPassword: %s" % ahora.microsecond
                fd.write(linea4)
                fd.write('\n')
                linea5 = "uid: %s" % nombre
                fd.write(linea5)
                fd.write('\n')
		fd.write('\n')
        fd.close()
if __name__ == '__main__':
        main()
