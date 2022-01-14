# Author: Tom Storey
# Date 22/10/2021
# Objective Shape Calculator

shape_type = [(1,"Trapezoid"), (2,"Parallelogram"),(3,"Rectangle"),(4,"Square"),(5,"Triangle"),(6,"Circle")]


def int_input(descriptor, lowest, highest):
    var = ""
    while not var.isnumeric():
        var = input(f"Enter value for {descriptor} between {lowest} - {highest} > ")
    else:
        while (int(var) < lowest or int(var) > highest):
            var = ""
            while not var.isnumeric():
                var = input(f"Error, Enter value for {descriptor} between {lowest} - {highest} > ")
    return int(var)

def float_input(descriptor):
    val = ""
    while True:
        try:
            return float(val)
        except ValueError:
            val = input(f"Enter the {descriptor} > ")

def trapezoid_function():
    vert1 = float_input("Vertices 1")
    vert2 = float_input("Vertices 2")
    vert3 = float_input("Height 3")
    value = round((vert1 + vert2)/2 * vert3,2)
    print(f"Area > {value} \n")

# def parallelogram_function():
#
# def rectangle_function():
#
# def square_function():
#
# def triangle_function():
#
# def circle_function():

while True:
    start = input("continue/exit (y/n) > ").upper()
    if (start != "Y"):
        exit()
    else:
        print(shape_type)
        shape_selection = int_input("shape selection", 1, 6) - 1
        if ( shape_selection == 0 ):
            trapezoid_function()
        if ( shape_selection == 1 ):
            trapezoid_function()
        if ( shape_selection == 2 ):
            trapezoid_function()
        if ( shape_selection == 3 ):
            trapezoid_function()
        if ( shape_selection == 4 ):
            trapezoid_function()
        if ( shape_selection == 5 ):
            trapezoid_function()

