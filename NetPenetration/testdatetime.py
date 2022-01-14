import time
from datetime import datetime

def timeprint():
    return datetime.now()

x = str(datetime.now())
y = datetime.now()
print("x", x)
print("y", y)
print("f", timeprint())
time.sleep(5)
print("x", x)
print("y", y)
print("f", timeprint())


target = "192.168.0.1"
filename = str(target)+str(timeprint()) + ".txt"
print (filename)
f = open(filename, "w+")

f.write(filename)
f.close()

openport = ["a","b","c"]
contents = str(target), str(timeprint()), "\n", *openport

print(str(contents))

namedtime= time.localtime()
timesimp = time.strftime("%d, %H:%M:%S", namedtime)
print(timesimp)