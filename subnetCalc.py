#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  subnetCalc.py
#  
#  Copyright 2021 butts <butts@BUTTS-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import ipaddress, os, time
import socket, struct


def main(args):
	print ("WeLcOmE!! to the Subnet Calculator!")
	print ("by: K Marshall")
	time.sleep(3)
	os.system("cls")
	
	print ("Enter the ip address")
	string = input()
	interger = ip2long(string)	
	binary = "{0:b}".format(interger).zfill(8)
	print("In binary, this is... \n" +binary)
	time.sleep(1)
	os.system("cls")
	
	print("Now enter a subnet mask. use '/n' or 'x.x.x.x'")
	subMask = input()
	os.system("cls")
	
	if subMask[0]=="/":
		print ("CIDR notation. in binary this mask is...")
		subBinStr = ""
		counter = int(subMask[1:])
		bitCount=32
		
		while counter >= 1:
			subBinStr = subBinStr + "1"
			counter -=1
		
		subBin = subBinStr.ljust(32,"0")
		print (subBin+"\n")
		print ("Your chosen IP was...\n" + string + "\n")
		print ("In binary, thats...\n" + binary +"\n")
		
		network = ipaddress.IPv4Network(string + subMask, strict=False)
		print("Your Net Address is... \n"+str(network.network_address) + "\n")
		
		print("Your available hosts are...")

		hosts = list (network.hosts())
		n = len(hosts) - 1
		print ( str(hosts[0]) + " - Through - " + str(hosts[n]) + "\n")
		
		print("And your broadcast address is... \n" + str(hosts[n]+1) + "\n")
		

	elif subMask[0].isdigit() == True:
		print ("octet")
		network = ipaddress.IPv4Network(string + "/" + subMask, strict=False)
		print ("Your chosen IP was...\n" + string + "\n")
		print ("In binary, thats...\n" + binary +"\n")
		print("Your Net Address is... \n"+str(network.network_address) + "\n")
		
		print("Your available hosts are...")

		hosts = list (network.hosts())
		n = len(hosts) - 1
		print ( str(hosts[0]) + " - Through - " + str(hosts[n]) + "\n")
		
		print("And your broadcast address is... \n" + str(hosts[n]+1))
		
	else:
	 print("You done fucked up, kid")


	return 0
	
def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
