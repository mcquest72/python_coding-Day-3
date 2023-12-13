"""This program interprets the Body Mass Index BMI
based on a user's weight and height"""

height = float(input('enter your height in m: '))
weight = float(input('enter your weight in kg: '))

BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f'Your BMI is {BMI}, you are underweight')
elif 18.5 < BMI < 25:
    print(f'Your BMI is {BMI}, you have a normal weight')

elif 25 < BMI < 30:
    print(f'YOur BMI is {BMI}, you have a slightly overweight')

elif 30 < BMI < 35:
    print(f'Your BMI is {BMI}, your are obese')

else:
    print(f'Your BMI is {BMI}, you are clinically obese')
