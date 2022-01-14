shopping_list = ["eggs", "eggs","milk", "fish", "meat", "flour", "foil"]
lucky_numbers= [18, 1, 12, 8, 16, 4]
print(shopping_list[0])
print (shopping_list[-1])
print (shopping_list[0:3])
shopping_list[2]= "milk"
print (shopping_list [2])

shopping_list.extend(lucky_numbers)
shopping_list.append("shoes")
shopping_list.insert(2, "bag")
lucky_numbers.sort()
print (shopping_list)
print(shopping_list.index("eggs"))
print(shopping_list.count("eggs"))
print(lucky_numbers)

shopping_list2= shopping_list.copy()
print (shopping_list2)
