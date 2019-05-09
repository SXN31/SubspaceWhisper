#!/usr/bin/python
# 
# Filename:  romulan_prefixes.py
#
# Version: 1.0.1
#
# Author:  Professor James Moriarty
#
# Summary:  Appends or removes random 6-char string of [a-z,0-9] plus 
# ".cloudfront.net" to each line of a file that's been Cloakified using 
# cloudfront_prefixes cipher.
#
# Description:  
#

import os, sys, getopt, random

gCharList = "abcdefghijklmnopqrstuvwxyz0123456789"

if ( len(sys.argv) != 2 ):

	print "usage: romulan_prefixes.py <cloakedFilename>"
	print
	exit

else:

    with open( sys.argv[1], "r" ) as file:

            cloakedFile = file.read().splitlines()

    with open( sys.argv[1], "w" ) as file:

        for i in cloakedFile:

            count = 0
            subdomainNoise = ""

            while ( count < 7 ):
                subdomainNoise = subdomainNoise + gCharList[ (random.randint(0,35)) ]
                count = count + 1

            subdomainNoise = subdomainNoise + ".stareempire.romulan.subspace"

            file.write( i + subdomainNoise + "\n" )

