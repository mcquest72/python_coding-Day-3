# This code prints out the pass to ride a roller coaster

print()
print('Welcome to the roller coaster')

height = int(input('Whats is your height'))

if height >= 120: 
    print('Come aboard the roller coaster')
    
    age = int(input('What is your age? '))
    if age <= 12:
        print('Your ticket is $5')
    elif age < 18 > 12:
        print('Your ticket is $7')
    else:
        print('Your ticket is $12')

else: 
    print('You need to grow taller to ride in the roller coaster')

    