
def trasnslate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaiou":
            translation = translation + "X"
        else:
            translation = translation + letter
    return translation


print(trasnslate("I Am Very Cool"))