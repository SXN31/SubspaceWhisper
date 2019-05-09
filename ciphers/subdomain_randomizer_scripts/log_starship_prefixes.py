8#!/usr/bin/python
# 
# Filename:  log_starship_prefixes.py
#
# Version: 1.0.0
#
# Author:  Professor James Moriarty
#
# Summary:  Appends or removes random 8-digit string plus ".starship.starfleet.federation.subspace" 
# to each line of a file that's been Cloakified using log_subspace_prefixes cipher.
#
# Description:  
#
# Random Strings Generated from https://www.random.org/strings/?num=66&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new

import os, sys, getopt, random

gCharList = "abcdefghijklmnopqrstuvwxyz0123456789"

if ( len(sys.argv) != 2 ):

	print "usage: starship_prefixes.py <cloakedFilename>"
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

            subdomainNoise = "NCC-" + subdomainNoise + ".starship.starfleet.federation.subspace"

            file.write( i + subdomainNoise + "\n" )