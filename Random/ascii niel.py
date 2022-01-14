f = open("ascii_art.txt,"r"")
lines = f.readlines()
ascLines = []
for line in lines:
 chars = list(line)
 asc = [ord(i)for i in chars]
 ascLines.append(asc)


f = open ("ascii_vals.txt", "w")
for line in ascLines:
    artLine = line.join(",")
    f.write(artLine)

f.close()