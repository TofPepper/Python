# a tuple is an immutable data structure that can not be modified once it is defined

# it is created by placing all the items in parantheses () but it is optional

#creating a tuple with one element
var1 = ("elemtent1",)
print("This is a tuple of one element: ", var1)
print(type(var1))

#since () is optional
var2 = 2050, 
print("Since () is optional, this is a tuple of one element created without (): ", var2 )
print(type(var2))

#accessing tuple elements using indexing
number = (2, 5, 6, 7, 34,2, 2, 68,2, 2, 51, 22, 60, 78)
print("This is the first item index 0: ", number[0])
print("This is the last item index -1: ", number[-1])

#counting the number a particular item occured
print("The number of times 2 occured is: ", number.count(2))

#printing the index of a particular item in a list
print("Number 34 is at the index: ", number.index(34))