# Favorite Places:
# Make a dictionary of favorite places with the persons name as the kep.
# Create a list as one of the items in the dictionary that contains one or
# more favorite places.

favorite_places = {
    'terry': ['wild cat rock', 'mount mitchell', 'grandfather mountain'],
    'carlee': ['blue ridge parkway', 'tweetsie', 'boone', 'carter falls',
               'cave', 'burger king'],
    'linda': ['thrift store', 'home', 'little switzerland', 'sparta'],
    'rebekah': [],      # let's have one blank and know how to check it
}

# If you leave off items, the default behavior of the for loop is to 
# return the key and the value.
# for name, place in favorite_places.items():
for name, places in favorite_places.items():
    if places:
        print(f"{name.title()} has {len(places)} favorite places:")
        print("\t", end="")
        for place in places:
            # doing trailing comma control...
            if place == places[-1]:     # [-1] returns last item in list
                print(f"{place.title()}", end="")
            else:
                print(f"{place.title()}, ", end="")
    else:
        print(f"{name.title()} doesn't have any favorite places defined yet.")        
    print("\n")