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
import ipaddress
import socket, struct


def main(args):
	print ("welcome to the Subnet Calculator")
	print ("enter the ip address")
	string = input()

	interger = ip2long(string)	
	binary = "{0:b}".format(interger).zfill(8)
	print("in binary, this is - \n" +binary)
	
	print("Now enter a subnet mask. use '/n' or 'x.x.x.x'")
	subMask = input()
	
	if subMask[0]=="/":
		print ("CIDR notation. in binary this is...")
		subBinStr = ""
		counter = int(subMask[1:])
		bitCount=32
		
		while counter >= 1:
			subBinStr = subBinStr + "1"
			counter -=1
		
		subBin = subBinStr.ljust(32,"0")
		print (subBin)
		
		network = ipaddress.IPv4Network(string + subMask, strict=False)
		print("your Net Address is : \n"+str(network.network_address))
		
		print("your available hosts are... \n")

		hosts = list (network.hosts())
		n = len(hosts) - 1
		print ( str(hosts[0]) + " - Through - " + str(hosts[n]))
		
		print("and your broadcast address is - \n" + str(hosts[n]+1))
		

	elif subMask[0].isdigit() == True:
		print ("octet")
		network = ipaddress.IPv4Network(string + "/" + subMask, strict=False)
		print("your Net Address is : \n"+str(network.network_address))
		
		print("your available hosts are... \n")

		hosts = list (network.hosts())
		n = len(hosts) - 1
		print ( str(hosts[0]) + " - Through - " + str(hosts[n]))
		
		print("and your broadcast address is - \n" + str(hosts[n]+1))
		
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
