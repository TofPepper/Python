#python dictionary stores element in key/value pairs

#dictionary of states and capital in Nigeria
nigeria_States = {
    "Abia" : "Umahia",
    "Adamawa" : "Yola",
    "Akwa-Ibom" : "Uyo",
    "Anambra" : "Akwa",
    "Bauchi" : "Bauchi",
    "Bayelsa" : "Yenagoa",
    "Benue" : "Makurdi", 
    "Borno" : "Maiduguri",
    "Cross-River" : "Calabar",
    "rty" : "nvueu",
    "Delta" : "Asaba",
    "Ebonyi" : "Abalaiki", 
    "Edo" : "Benin-City",
    "Ekiti" : "Ado-Ekiti"
}


print(nigeria_States)

print("")

#deleting an element in a dictionary
del nigeria_States["rty"]
print("Corrected states and capital of Nigeria: ", nigeria_States)
print("")

#accessing elements in a dictionary
print("The capital of Cross-River in Nigeria is: ",nigeria_States["Cross-River"])
print("")

#iterating
for states in nigeria_States:
    print(states)

#dictionary of different data types
number_Categories = {
   1 : "Odd" ,
   2 : "Even",
   3 :  "Odd",
   4 :  "Even",
   5 :  "Odd"
}
print("Initial Dictionary",number_Categories)

#adding elements to a dictionary
number_Categories[6] = "Even"
number_Categories[7] = "Even"
print("Updated Dictionary: ", number_Categories)

#cahnging elements in this dictionary because 7 is Odd not Even
number_Categories[7] = "Odd"
print("Corrected dictionary: ", number_Categories)

#accessing element in a dictionary using its key value
print("Is 5 an odd number or an even number? ", number_Categories[5])

#you can also delete a dictionary using this statement * del(name of the dictionary) *

#Python Dictionary Methods
# all()  => return True if all the keys in the dictionary are True (or if the dictionary is empty)
# any()  => returns true if any of the dictionary is true, returns False if the dictionary is empty
# len()  => returns the length(the number of items) in the dictionary
# sorted()  => returns a new sorted list of keys in the dictionary
# clear()  => removes all items from the dicionary
# key()  => returns a new item of the dictionary's keys
# values()  => returns a new object of the dictionary's values

#dictionary memebership
squares = {1:1, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
print(squares)
print("")
print("")
print(1 in squares) #it should return True
print("")
print(2 not in squares) #it should return True
print("")
print(49 in squares) #it should be false

#iterating
for i in squares:
    print(i)