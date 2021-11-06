import math

n = 0

i = int(input('Enter the number of items: '))
b = int(input('Enter the number of items per box: '))

def num_boxes():
    n = math.ceil(i / b)
    print(f'For {i} items, packing {b} items in each box, you will need {n} boxes.')

num_boxes()