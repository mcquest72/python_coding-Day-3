 # This program runs pizza order based on customer's input

print()
print('Welcome to Python Pizza Deliveries')
bill = 0

print()
size = input('What size Pizza do you want? s, m, or l ')

if size == 's':
    bill = 15
    print('Small size Pizza is $15')

elif size == 'm':
    bill = 20
    print('Medium size Pizza is $20')

else:
    bill = 25
    print('Large size Pizza is $25')


print()
add_pepperoni = input('Do you want pepperoni? y or n ')

if add_pepperoni == 'y':
    bill += 2

print()
extra_cheese = input('Do you want extra cheese? y or n ')

if extra_cheese == 'y':
    bill += 1

print(f'Your final bill is ${bill}')
