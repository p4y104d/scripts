#!/usr/bin/env python2.7
import sys
import urllib2


cadena = sys.argv[1]
s = urllib2.unquote(cadena)
print ("El string es: "+s)