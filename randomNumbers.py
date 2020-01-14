import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here with 'for' loop. Where is "number" in "my_randoms"? is numbers referring to the things in the range of "my_randoms"?
    
    if number in my_randoms:
        the_numbers_match = True

    if the_numbers_match:
        print(f'my_randoms list contains {number}')
    else:
        print(f'my_randoms list does not contain {number}')

    # Does my_randoms contain number? Change the boolean.

    # print(f'{number} is in the random list')

 