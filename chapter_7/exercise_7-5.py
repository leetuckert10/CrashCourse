# Movie Tickets:
#   Write a loop that prompts for a movie goers age and determine the cost
# of their ticket. Under age 3 is zero. Age 3 to 12 is $10. Age 13 and over
# is $15. Exit the loop on an input on an input value of zero.

flag = True

print("Please enter your age to determine your ticket price.")
print("Enter 0 to exit the application...")

while flag:
    age_string = input("Age: ")
    age = int(age_string)
    if age == 0:
        flag = False
    elif age <= 3:
        print("Your get in for free!") 
    elif 3 < age <= 12:
        print("Your cost is $10...")
    else:
        print("Your cost is $15...")
    print("")
print("Thank you for using my movie ticket app!")