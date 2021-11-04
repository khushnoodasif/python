#create function to loop random number generator

def random_number_generator():
    import random
    random_number = random.randint(1,100)
    return random_number
print(random_number_generator())

list_of_numbers = [1,3,4,5,6,7,8,9,10,11,12]