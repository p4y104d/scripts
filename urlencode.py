#!/usr/bin/env python2.7
import sys
import urllib2


cadena = sys.argv[1]

u = cadena.encode('utf-8')
s = urllib2.quote(cadena)
print ("El string es: "+s)