#list of numbers
numbers = [12, 45, 67, 55, 23, 43]
print("List before adding :", numbers)

#accessing the last item (index -1)
print("The last numer in the list",numbers[-1]) #it will return 43

#append adds an item to the end of a list
numbers.append(345)
print("List after adding some numbers", numbers)


#accessing item at index 0
print("The first number in the list",numbers[0]) #it will return 12

#extend() adds all items in a list to another list
odd_Numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print("Odd numbers", odd_Numbers)
numbers.extend(odd_Numbers)

print("List after adding odd numbers to existing numbers list", numbers)

#iterating through a list
for number in numbers:
    print(number)

#creating lists using list comprehension
digits = [digit*digit for digit in range (1,10)]
print("A list created by list comprehension: ", digits)

digits2 = [digit2+digit2 for digit2 in range (1,10)]
print("A list created by list comprehension: ", digits2)

#an empty list
empty_list = []
print("An empty list",empty_list)

#list of mixed data type
mixed_List = [12, 56.89, True, "Python"]
print("A list that contains mixed data type",mixed_List)

#changing list items
mixed_List[2] = False
print("List after changing (True) to (False):", mixed_List)

#deleting an item from a list 
#using del
mixed_List.append("mistake")
print("List after adding mistake:", mixed_List)
del mixed_List[-1]
print("List after deleting mistake:", mixed_List)
#using remove
mixed_List.append('error')
print('List after including a text at the end:', mixed_List)
mixed_List.remove('error')
print("List after deleting the text: ", mixed_List)

#list slicing, selecting more than one item in a list
word = ["P", "R", "O", "G", "R", "A", "M", "M", "I", "N", "G", "L", "A", "N", "G", "U", "A", "G", "E"]
print("Items at index 2 to index 4",word[2:5]) #prints items at index 2 to index 4
print("Items at index 5 tothe end",word[5:]) #prints items at index 5 to the end
print("All items in the list",word[:]) #prints all items in the list

#other Python list methods

#insert() => inserts an item at a specified index
#pop() => returns and removes items present at the given index
#clear() => removes all items from the list
#index() => returns the index of the first matched item
#count() => returns the count of the specified item in the list
#sort() => sorts the list in ascending or desceding order
#reverse() => reverses the items of the list
#copy() => returns the shallow copy of the list
