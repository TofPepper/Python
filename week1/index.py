name = "Emmanuel Tofunmi"
age = 19
gender = "Female"

print(name)

languages = ["HTML", "JS", "python", 29]
print(languages)

print(languages[1])

a,b,c,d = 5, 7, "Hello world", True
print(a) 
print(b) 
print(c) 
print(d)

products = ('XBox', 499.99, "Habibi", 23)
print(products)
print(products[2])

student_ids = {112, 114, 117, 113}
print(student_ids)

capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)

#assignment operator (a = 7)
# addition assignment (a += 1 # a = a + 1)
# subtraction assignment (a -= 3 # a = a - 3)
# multiplication assignment (a*= 4 # a = a * 4)
# division assignment ( a /= 3 # a = a/3 )
# remainder assignment ( a %= 10 # a = a % 10)

x = str(10)
y = int(10)
z = float(10)
print("x = " , x)
print("y = ", y)
print("z = ", z)



print(type(capital_city))
print(type(student_ids))
print(type(a))
print(type(gender))
print(type(age))

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

name = input("Enter your name")
print("Welcome!" + name)

#Project Number 1
username = input("Hey there! What is your name?__")
color = input("Hmmmmm, what a nice name! What is your favourite colour? ___")
print("Hey " + username + ". Your favourite color, " + color + " is amazing!")


# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))
