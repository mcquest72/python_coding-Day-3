# This program lets you ride and take a picture on a roller coaster.

print()
print('Welcome to the roller coaster')

print()
height = int(input("What's your Height? "))
bill = 0

if height > 120:
    print('Welcome onboard comrade')
    print()

    age = int(input("What's your age? "))

    if age < 12:
        bill = 5
        print('Child tickets is $5')

    elif age < 18 > 12:
        bill = 7
        print('Youth tickets is $7')

    else:
        bill = 12
        print('Adult tickets is $12')

    print()

    photos = input('Do you want photos? Y or N ')
    if photos == 'Y':
        bill += 3

    print()
    print(f'Your final bill is ${bill}')

else:
    print('Sorry, you need to grow taller to ride the roller coaster')
