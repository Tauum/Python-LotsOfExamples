lyrics = " London Bridge is falling down \n Falling down, falling down \n London Bridge is falling down \n My fair lady \n\n Build it up with iron bars \n Iron bars, iron bars \n Build it up with iron bars \n My fair lady \n\n Iron bars will bend and break \n Bend and break, bend and break \n Iron bars will bend and break \n My fair lady \n\n Build it up with god and silver \n Gold and silver, gold and silver \n Build it up with gold and silver \n My fair lady \n\n London Bridge is falling down \n Falling down, falling down \n London Bridge is falling down \n M-y-y f-a-i-r l-a-d-y "
lyrics = lyrics.upper()
list1 = list(lyrics.split())
print (list1)
print ('London  shows: ',list1.count('LONDON'))
print ('Bridge  shows: ',list1.count('BRIDGE'))
print ('lady  shows: ',list1.count('LADY'))
print ('falling  shows: ',list1.count('FALLING'))


