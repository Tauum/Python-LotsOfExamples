squares = 5

result = list(map(lambda x: 2 ** x, range(terms)))

for i in range(squares):
 print("2 raised to the power of",i,"is",result[i])
