import random

# creates dictionary
phonebook = {}
phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""


print()
print("*****  start section 1 - print dictionary ********")
print()


mydictionary = dict(m=8, n=9)
print(mydictionary)

print(len(phonebook))  # values in dictionary
print(type(phonebook))  # type


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

# returns value
# print(phonebook["Chris"])

# can save value into variable
# phone = phonebook["Chris"]
# print(phone)

name = "chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in phonebook")



print()
print("*****  end section 2 ********")
print()





print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook["Chris"] = "555-0123"    #updated number
phonebook["Joe"] = "555-4444"      #appended number

print(phonebook)

print()
print("*****  end section 3 ********")
print()





print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)

del phonebook["Chris"]      #deletes Chris' number, only if it finds match

print(phonebook)


print()
print("*****  end section 4 ********")
print()





print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

for key in phonebook:
    print(f"the key is {key} and the value is {phonebook[key]}")
    # gets the name and matching phone number


for value in phonebook.values():
    print(value)


for key, value in phonebook.items():
    print(f"the key is {key} and the value is {value}")


for ph_tuple in phonebook.items():
    print(ph_tuple)
    # creates tuple, immutable, splits it up for you


print()
print("*****  end section 5 ********")
print()





print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get(
    "chris", "999"
)  # displays value or different value if first is not found
print(phone)

phonebook.clear()  # clears phonebook but does not delete it
print(phonebook)


print()
print("*****  end section 6 ********")
print()



print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris", "not found")  # removes value from dictionary
print(remove)
print(phonebook)

print()
print("*****  end section 7 ********")
print()



print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem()  # only pops out last item

print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()

"""

print()
print("*****  start section 9 - using random and converting to list ********")
print()

phonebook_list = list(phonebook)  # default option is key
print(phonebook_list)

random_key = random.choice(phonebook_list)  # only works on lists
print(random_key)
print(phonebook[random_key])  # prints key with associated value

print(phonebook[random.choice(list(phonebook))])  # does all of the above on one line


print()
print("*****  end section 9 ********")
print()
