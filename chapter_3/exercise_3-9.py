guests = ['Martin Luther', 'John Calvin', 'Donald Trump', 'King David']

# Donald cannot make it. Nancy Pelosi wants give him a ride :D
# Let's invite Adam and Eve instead!
guests[2] = 'Adam and Eve'
print(guests)

guests.insert(0, "Geof Myers")		# insert at first position
guests.insert(2, "John Allgood")	# insert at third position
guests.append("Greg Syfan")			# stick it on the end
print(guests)

print(f"Hey! I found a biggger table so I am inviting {len(guests)} guests:")
print(f"{guests[0]}, please join me for supper!")
print(f"{guests[1]}, please join me for supper!")
print(f"{guests[2]}, please join me for supper!")
print(f"{guests[3]}, please join me for supper!")
print(f"{guests[4]}, please join me for supper!")
print(f"{guests[5]}, please join me for supper!")
print(f"{guests[6]}, please join me for supper!")