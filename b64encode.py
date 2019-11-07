#!/usr/bin/env python2.7
import sys
import base64

cadena = sys.argv[1]

u = cadena.encode('utf-8')
s = base64.b64encode(cadena)
print ("El string es: "+s)
