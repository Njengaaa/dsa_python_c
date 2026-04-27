import random

def max_min(numbers):
    minimum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
            
        
            
    return minimum

def getvalues():
    list = random.sample(range(50, 100), k=10)
    print(list)
    result = max_min(list)
    print(f"value is {result}")
    
getvalues()