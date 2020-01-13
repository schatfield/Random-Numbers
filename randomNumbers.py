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

    if (the_numbers_match == False):
        print (f'{number} is not the random list')
    else:
        print(f'{number} is in the random list')

    # Iterate your random number list here

    # Does my_randoms contain number? Change the boolean.

    # print(f'{number} is in the random list')

#     name = "Joe"
# if (name == "Steve"):
#     print ("I feel great")
# elif (name == "Joe"):
#     print ("You got the better instructor")
# else:
#     print("I have a cold")
