import random

def binary_recursion(values, target,low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_recursion(values,target,low,mid -1)
    else:
        return binary_recursion(values,target,mid + 1,high)
    
def get_values():
    values = random.sample(range(-10,10), k=5)
    values = sorted(values)
    print(f"Values: {values}")
    target = int(input("Enter the target value: "))
    result = binary_recursion(values, target,low=0 ,high=len(values-1))
    
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Not found")
        
    