#it is also immutable like Tuple
# a set of integer type
matricNo = {386, 384, 389, 345, 224}
print("Matric Number: ", matricNo)

#a set of string type
vowels = {'a', 'e', 'i', 'o', 'u'}
print("Vowel letters: ", vowels)

#a set of mixed data type
mixed_set = {"name", 45, 4.7, -9, True}
print("Set of mixed data type: ", mixed_set)

#an empty set
empty_set = set ( )
print("Data type of empty set is: ", type(empty_set))

#duplicate items in a set
numbers = {2, 4, 4, 4, 8, 5, 6, 6, 7, 8, 8}
print(numbers)

letters = {'a', 'd', 's', 'd', 'f', 'g', 'd', 'd', 's', 'a'}
print(letters)
print('Number of letters are: ', len(letters))

#adding items to a list
matricNo.add(486)
print('Updated Matric Number: ', matricNo)

#adding two sets together
utensils = {'spoon', 'knife', 'plates', 'bowl'}
fabrics = {'table cloth', 'curtains', 'dish linen'}
print(utensils)
print(fabrics)
utensils.update(fabrics)
print("What can be found in the kitchen: ", utensils)

#removing an element from set
utensils.add(345677)
print('Set before removal: ', utensils)

removedValue = utensils.discard(345677)
print('Set after removal of the integer: ', utensils)

#iterating over a set
for utensil in utensils:
    print('Items that can be found in the kitchen: ',utensil)

#finding the number of items in a set
print('Total elements in this set of utensils: ', len(utensils))

#Pyhton Set Operations
A = {1, 2, 3, 4, 5}
A1 = {1, 2, 3, 4, 5, 7}
A2 = {1, 2, 3, 4, 5, 7}
B = {2, 3, 4, 5, 6, 7, 9}
C = {1, 3, 5, 7, 9, 11}
D = {2, 4, 6, 8, 10, 12}
#UNION
print('Union of Set A and Set B: ', A|B)
print("")
print('Union of Set B and Set D: ', B.union(D))
#INTERSECTION
print('Intersection of Set A and Set B: ', A&B)
print('')
print('Intersection of Set C and Set D: ', C.intersection(D)) #it should return an empty set
#DIFFERENCE BETWEEN TWO SETS
print('Difference between Set A and Set B: ', A - B)
print('')
print('Difference between Set C and Set D: ', C.difference(D))
#SYMMETRIC DIFFERENCE
print('Symmetric difference between Set B and Set C: ', B^C)
print("")
print('Symmetric Difference between Set C and Set D: ', C.symmetric_difference(D))
#EQUALITY OF SETS
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
print('')
if A1 == A2:
    print('Set A1 and Set A2 are equal')
else:
    print('Set A1 and Set A2 are not equal')