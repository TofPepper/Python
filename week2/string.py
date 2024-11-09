
#strings are also immutable like sets and tuples

#indexing
greeting = 'hello'
print(greeting[0])
print(greeting[-4])

#slicing
print(greeting[1:])
print(greeting[:])
print(greeting[2:4])

#assigning a variable name to a new string
greet = 'bonjour'
print('Greetings in French: ', greet)
greet = 'Good morning'
print('Greetings in English: ', greet)

#Python Multi-line String
songs = """
E ti tobi to o
Iba
Worthy of my Praise
Oba awon Oba
Omo Oba
"""
print('Songs on my playlist: ', songs)

#String Operations
#COMPARING TWO STRINGS
s1 = 'Hello World'
s2 = 'Good Morning'
s3 = 'Hello World'
print('Is string in S1 the same as the string in S2? ',s1 == s2)
print('Is string in S1 the same as the string in S3? ', s1 == s3 )
#JOINING TWO OR MORE STRINGS
greet1 = "Hello, "
name1 = "Tofunmi. "
role = "You are a student."
sentence = greet1 + name1 + role
print(sentence)
#ITERATING
for word in name1:
    print(word)
#LENGTH
print('Number of letters in my songs: ', len(songs))
#STRING MEMBERSHIP TEST
print('o' in 'Tofunmi') #true
print('fun' not in 'Tofunmi') #false
#ESCAPE SENTENCES
question = "He said, \"What's there?\""
question2 = 'He said, "What\'s there?"'
print(question)
print('')
print(question2)


name2 = "Charis"
country = "Uk"
print(f'{name2} is from {country}')