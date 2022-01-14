monthConversion = { # keys can also be any number or string aslong as they are unique
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConversion["Dec"])

#passing a default value incase the requestd doesnt exist
print(monthConversion.get("abc", "value doesnt exist"))


input = input("Enter the first 3 letters of a month \n >")
selected = monthConversion[input]
print(selected)
