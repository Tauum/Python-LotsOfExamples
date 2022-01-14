menu = 1

while menu == 1:
    print ("     ||  MENU || ")
    print("")
    print( "1.  Polyalphabetic  ")
    print("")
    print("}-------------------{")
    print("")
    print("2.   List maths      ")
    print("")
    print("}-------------------{")
    print("")
    print("3.Fiboncii sequence ")
    print("")
    print("}-------------------{")
    inputmenu = ""
    inputmenu = input("-{[Please enter which function you'd like to use]}-")
    print("enter menu to return menu ")
    menu +=1

while menu == 2:
    if inputmenu == "1":
        import cyther.py
    if inputmenu == "2":
        import algorithm.py
    if inputmenu == "3":
        import Fibonaccisequence.py