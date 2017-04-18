# input exercise 1-3
name = input("What is your name?\n")
upper_name = name.upper()
counter = 0
for i in name:
    counter += 1
print ("Please fill in the blanks below:____(name)____'s favorite subject in \
           school is ___(subject)___.")
fav_subject = input("What is subject?\n")
print ("Hello, %s" % upper_name)
print ("Your name has %d" % counter)
print ("%s's favorite subject in school is %s." % (name, fav_subject))

# 3-5 Day of week
list_for_days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
users_day = int(input("Day (0-6)?\n"))
if users_day in (0, 6):
    print ("Go to work.")
else:
    print ("Sleep in.")
print (list_for_days[users_day])

# 6 C to F
users_temp_in_C = float(input("Temperature in C?\n"))
convert_temp_to_F = users_temp_in_C * 1.8 + 32
print ("Temp in C:%f, Temp in F:%f" % (users_temp_in_C, convert_temp_to_F))

# 7-8 Tip calculator
total_bill_amount = float(input("Total bill amount?\n"))
level_of_service = input("Level of service?\nPut good, fair, or bad.\n")
levels = {"good": 0.2, "fair": 0.15, "bad": 0.1}
if level_of_service not in levels:
    print ("wrong input.")
for level in levels.keys():
    if (level_of_service == level):
        tips = total_bill_amount * levels[level]
print ("Tips:{:.2f}".format(tips))
number_of_ppl = int(input("Split how many ways?\n"))
amount_per_person = total_bill_amount / number_of_ppl
print ("Total amount:{:.2f}, amount per person:{:.2f}".format(total_bill_amount, amount_per_person))


# 9. using while loop to print out number 1 to 10
i = 1
while i < 11:
    print ("%d" % i)
    i += 1

# 10. How many coins?
want_coins = True
coins_have = 0
while want_coins:
    print ("You have %d coins" % coins_have)
    print ("Do you want another coin?")
    users_answer = input("Y or N.\n")
    if (users_answer == "Y"):
        coins_have += 1
    else:
        want_coins = False
