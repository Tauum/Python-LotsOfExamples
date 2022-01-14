readFile = open("/Users/mac/Desktop/untitled folder/read.rtf", "r")
writeFile = open("/Users/mac/Desktop/untitled folder/write.rtf", "w")
EOF = False

a
b
c

if input >10:
    print(", ")
if input >20:
    print(", ")

elif input 0: < 10:
    while not EOF:
        line = readFile.readline()

    if line == "":
        EOF = True
    else:
        # line = line.replace("#", " ")
        print
        line

        for char in list(line):
            ascii = str(ord(char)) + ","
            writeFile.write(ascii)

    writeFile.write("\n")