def is_float(value) :
    try:
        float(value)
        print("float value")
        return True
    except ValueError:
        print("non float value")
        return False
print(is_float(3.14))
print(is_float("a"))
