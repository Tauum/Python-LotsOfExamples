firstName = 'Amanda'
lastName = 'Cox'

#basic stuff
sentence = 'My name is {} {}'.format(firstName, lastName)
print(sentence)

# alternate
sentence2 = f'my name is {firstName.upper()} {lastName.upper()}'
print(sentence2)

#object basic
person = {'name': 'Benny', 'age':'15' }
print("person object= {}".format(person))
print("person variables= {} {}".format(person['name'], person['age']))

#alternate
sentence3 = f'my name is {person["name"]} i am {person["age"]} years old' # < cannot have both outer and inner same quotation type
print(sentence3)

#calculation 
calc = f'4 times 11 equals {4*11}'
print(calc)

#loop
for n in range(1,4):          #V 0 is padding and 2 is ammount of digits
    sentence4 = f'value is {n:02}'
    print(sentence4)

#floats
pi = 3.14159265      # V shortening to 4 digits  F is floating point
sentence5 = f'pi = {pi:.4f}' # this actually rounds the number too which is nice
print(sentence5)

#dates
from datetime import datetime
birthday = datetime(1990, 1, 1) # by default includes time of 00:00:00
sentence6 = f'my birthday is on {birthday}'
print(sentence6)
sentence7 = f'my birhtday is on {birthday: %b %d, %Y}' # this is formatted to a string
print(sentence7)
