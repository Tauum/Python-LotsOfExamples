#!/bin/python3

import sys
import socket
import time

openport = []
banner = ("-" * 30)


def timeprint():
    namedtime = time.localtime()
    timeprint = time.strftime("%H:%M:%S", namedtime)
    return timeprint


print("\nCreated by T.S \nFile save is Portscan.txt\n")
print("------------------------------")
target = input("IP Target: ")
portmin = (input("Port min: "))
portmax = (input("Port max: "))
file = str(input("Save results (y/n): "))

if (target == "") or (file == "") or (portmin == "") or (portmax == ""):
    print("required information missing. \nQuitting.")
    sys.exit

else:
    portmin = int(portmin)
    portmax = int(portmax) + 1
    print(banner, "\nTarget: ", target, "\nPorts: ", portmin, "-", portmax, "\nTime: " + str(timeprint()), "\n", banner)
    continuescript = str(input("Continue? (y/n): "))
    if (continuescript == "Y") or (continuescript == "y"):
        print("------------------------------")
        try:
            for port in range(portmin, portmax):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)  # moves onto next port after 1 sec
                result = s.connect_ex((target, port))  # returns error (0)
                print("Checking {}".format(port))

                if result == 0:
                    print("{} Open".format(port))
                    openport.append(port)
                    s.close()  # closes port


        except KeyboardInterrupt:
            print("\nExiting Program.")
            sys.exit()
        except socket.gaierror:
            print("Hostname unresolved")
            sys.exit()
        except socket.error:
            print("Unable to connect to server")
            sys.exit()

    if (file == "n") or (file == "N"):
        info = '{0}' " - " '{1}' " - " '{2}' "\n".format(str(target), str(timeprint()), str(openport))
        print(str(info))
        print("Results unsaved.")
    else:
        f = open("portScan.txt", "a")
        info = '{0}' " - " '{1}' " - " '{2}' "\n".format(str(target), str(timeprint()), str(openport))
        f.write(str(info))
        f.close()
        print(str(info))
        print("Results Saved.")