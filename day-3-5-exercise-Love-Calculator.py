# Love Calculator
"""A program that tests the compatibility between two people"""

print('Welcome to the Love Calculator!')

# prompt user for input
name1 = input('What is your Name? \n')
name2 = input('What is their Name? \n')

# combine names for easy computation
combine = name1 + name2
lowerCase = combine.lower()

# Counting True love letters in user names
t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')

true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('o')
v = lowerCase.count('v')
e = lowerCase.count('e')

love = l + o + v + e

# getting the love score from user input
love_score = int(str(true) + str(love))

# using conditional statements to determine output
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos')

elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together')

else:
    print(f'Your score is {love_score}')

