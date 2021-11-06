import math

w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

v1 = math.pi * w ** 2 * a 
v2 = w * a + 2540 * d
v = v1 * v2 / 10000000000
print(f'The approximate volume is {v:.2f} liters.')
print('')
y_or_n = input('Would you like to buy tires with the dimensions entered (y/n)? ')
if y_or_n == 'y':
    pn = input('Please enter your phone number: ')
    print('Thank you, your information has been recorded. We will get into contact with you shortly.')
    open('volumes.txt', mode = 'rt')
    with open('volumes.txt', 'at') as volumes_file:
        print(f'{pn}', file = volumes_file)   
else:
    print('Okay, thank you for your time.')

from datetime import datetime
current_date_and_time = datetime.now()
#print(f"{current_date_and_time:%Y-%m-%d}")

open('volumes.txt', mode = 'rt')

with open('volumes.txt', 'at') as volumes_file:
    print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file = volumes_file)
    
