counter = 0

begin = str(input('Enter? (y/n): '))
if (begin == "y"):
    counter = counter + 1
    while counter >= 1:
            print('hello world' + "Counter:", counter)
            counter = counter + 1
            if (counter > 10):
                print("fin")
                break
else:
    print('bye m8')
