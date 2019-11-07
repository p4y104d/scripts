#!/usr/bin/env python2.7
import sys,base64

s = sys.argv[1]
e = base64.b64decode(s)
print ("El string decodeado es: "+e)
