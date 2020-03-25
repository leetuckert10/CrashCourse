guests = ['Martin Luther', 'John Calvin', 'Donald Trump', 'King David']

# Donald cannot make it. Nancy Pelosi wants give him a ride :D
# Let's invite Adam and Eve instead!
guests[2] = 'Adam and Eve'
print(guests)

# using insert and append to add to the list.
guests.insert(0, "Geof Myers")
guests.insert(2, "John Allgood")
guests.append("Greg Syfan")
print(guests)

print("Hey! I am sorry, but I can only feed to people. I am broke!")
uninvite = guests.pop()
print(f"{uninvite}, please keep your butt home!")
uninvite = guests.pop()
print(f"{uninvite}, please keep your butt home!")
uninvite = guests.pop()
print(f"{uninvite}, please keep your butt home!")
uninvite = guests.pop()
print(f"{uninvite}, please keep your butt home!")
uninvite = guests.pop()
print(f"{uninvite}, please keep your butt home!")

print(guests)

print(f"{guests[0]}, please join me for supper!")
print(f"{guests[1]}, please join me for supper!")

# now use the del method for deleting the last two
del guests[1]
del guests[0]
print(f"Use 'del' to empty the list: {guests}!")
