#!/usr/bin/python

import sys
import ldap

def usage():
	print "Usage: %s <server> <base> <user> <password>" % sys.argv[0]

def main():
	server = "ldap://" + sys.argv[1]
	base = sys.argv[2]
	user = sys.argv[3]
	password = sys.argv[4]
	filter = "(objectClass=inetOrgPerson)"
	print "Connecting to %s on %s" % (base, server)
	try:
		ldapclient = ldap.initialize(server)
		ldapclient.simple_bind(user, password)
		print "User connected: %s" % ldapclient.whoami_s()
		result = ldapclient.search_s(base=base, scope=ldap.SCOPE_SUBTREE, filterstr=filter)
		for line in result:
			print line[0]
		ldapclient.unbind_s()
	except Exception, e:
		print str(e)
if __name__ == '__main__':
	if len(sys.argv)<5:
		usage()
		sys.exit(1)
	main()
	
