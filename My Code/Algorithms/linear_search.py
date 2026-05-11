import random

def linear_search(values, target):
    for item in range(len(values)):
        if values[item] == target:
            return item
    return -1


def get_values():
    values = random.sample(range(10,20), k=5)
    print(f"Values: {values}")
    target = int(input("Enter the target value: "))
    result = linear_search(values, target)
    
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Not found")
        
get_values()