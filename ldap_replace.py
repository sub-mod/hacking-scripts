#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: sub-mod@redhat.com
import os
import sys

help = '''usage:
   ldap_replace.py <path of files> <LDAP_SERVICE_IP> 
'''

if len(sys.argv) <= 1:
    print help
    exit()

replacements = {'LDAP_SERVICE_IP': sys.argv[2]}

path = sys.argv[1]

for filename in os.listdir(path):
    print 'replacing in ' + filename
    with open(path + filename) as infile:
        lines = infile.readlines()
        with open(path + filename, 'w') as sources:
            for line in lines:
                for (src, target) in replacements.iteritems():
                    if src in line:

                        # print line

                        line = line.replace(src, target)

                        # print line

                sources.write(line)

