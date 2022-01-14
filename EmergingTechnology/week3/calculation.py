brickType = [ (1,0.65,0.1025,0.215), (2,0.73,0.1025,0.215), (3,0.53,0.1125,0.230), (4,0.68,0.1125,0.230), (5,0.73,0.1125,0.230), (6,0.80,0.1125,0.230)]
brickStyle = [ (1,"Antique Orange",4.54),(2,"Russet White",4.34),(3,"Natural Orange",5.02),(4,"Pulford Blend",5.30),(5,"Kilworth Blend",6.40),(6,"Mellow Russet",6.62),(7,"Plain Black",4.56),(8,"Weathered Red",4.74),(9,"Ember Blend",5.74),(10,"Olde Tudor",6.02),(11,"Tudor Black",5.42),(12,"Old Terracotta",5.80)]

def numberinput(descriptor):
    var = input(f"Enter the {descriptor} > ")
    while not var.isnumeric():
        var = input(f"Error, {descriptor} again > ")
    return int(var)

def areaCalc(height,length):
    return height * length

def noBricks(wall,brickSelection):
    return round(wall / (brickSelection[2] * brickSelection[3]),2)

def costCalc(ammount, cost):
    return round(ammount * cost,2)

while True:
    start = input("continue/exit (y/n) > ").upper()

    if (start != "Y"):
        exit()
    else:
        print("Brick-Types - format = [(id,depth,height,length)] (M)")
        print(brickType)
        typeSelection = numberinput("selection")
        print("Brick-Style - format = [(id,name,price)] (£)")
        print(brickStyle)
        styleSelection = numberinput("selection")

        brickTypeSelection = brickType[typeSelection-1]
        brickStyleSelection = brickStyle[styleSelection-1]

        height = numberinput("height (M)")
        length = numberinput("length (M)")
        wall = areaCalc(height,length)
        numberOfBricks = noBricks(wall,brickTypeSelection)

        waste = numberOfBricks * 0.05

        print(f"\nArea of wall> {wall}")
        print(f"No' Bricks > {numberOfBricks}")
        print(f"waste > {waste}")
        print(f"cost > {costCalc((numberOfBricks + waste), brickStyleSelection[2])}")  # < total cost