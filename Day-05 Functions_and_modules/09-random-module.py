import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print("Random Integer between 1 and 10:", random_integer)

rg = random.randrange(1, 11)  
# Generates a random integer between 1 and 10 (inclusive of 1, exclusive of 11)
print("Random Integer using randrange between 1 and 10:", rg)

choice = random.choice(['apple', 'banana', 'cherry'])
# Randomly selects an element from the given list
print("Random choice from the list:", choice)

uniform_random = random.uniform(1.0, 10.0)
# Generates a random float between 1.0 and 10.0
print("Random Float between 1.0 and 10.0:", uniform_random)

choices = random.choices(['red', 'blue', 'green'], k=5)
# Randomly selects 5 elements from the given list (with replacement)
print("Random choices from the list:", choices)

sample = random.sample(range(1, 20), 5)
# Randomly selects 5 unique elements from the given range (without replacement)
print("Random sample of 5 unique elements from range 1 to 20:", sample)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
# Shuffles the elements of the list in place
print("Shuffled List:", list)

