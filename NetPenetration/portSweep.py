
#!/bin/python3

import sys
import socket
import time
import os.path
from datetime import datetime

openport = []
banner = ("-" * 30)

def timeprint():
	namedtime = time.localtime()
	timeprint = time.strftime("%H:%M:%S", namedtime)
	return timeprint

#define target
print("\nStolen & modified Heath, Further modified by T.S \nFile save is Portscan.txt\n")
target = input("Target: ")
file = str(input("Save results (y/n): "))
portmin = (input("Port min: "))
portmax = (input("Port max: "))
if (target == "") or (file == "") or (portmin == "") or (portmax == ""):
	print("required information missing. \nQuitting.")
	sys.exit
else:
	portmin = int(portmin)
	portmax = int(portmax) + 1
	print(banner,"\nTarget: ",target,"\nTime: "+str(timeprint()), "\nPorts: ", portmin, "-", portmax,"\n",banner)
	continuescript = str(input("Continue? (y/n): "))
	if continuescript == "Y" or continuescript == "y":
		try:
			for port in range(portmin,portmax):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1) #float moves onto next port after 1 sec
				result = s.connect_ex((target,port)) # returns error (0)
				print("Checking port {}".format(port))
				if result == 0:
					print("Port {} is open".format(port))
					openport.append(port)
				s.close() #closes port

			print("\n",banner,"\n","OPEN: ",*openport,"\n",banner,"\n")

			if (file == "y") or (file == "Y"):
				f = open("portScan.txt", "a")
				info = '{0}' " - " '{1}' " - " '{2}' "\n".format(str(target),str(timeprint()), str(openport))
				f.write(str(info))
				f.close()
				sys.exit()

			elif (file == "n") or (file == "N"):
				print("Results unsaved.")
				sys.exit()
		except KeyboardInterrupt:
			print("\nExiting Program.")
			sys.exit()
		except socket.gaierror:
			print("Hostname unresolved")
			sys.exit()
		except socket.error:
			print("Unable to connect to server")
			sys.exit()
	else:
		print("Quitting")
		sys.exit
