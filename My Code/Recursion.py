import random

print("---------Direct Recursion------------------")
def basic(n: int):
    if n <0:
        return n
    print(n)
    return basic(n-1)

basic(5)


print("----------Indirect Recusion-----------------")
def a(n:int):
    if n > 0:
        print (f"Inside a {n}")
        return b (n-1)
    
def b(n:int):
    if n > 0:
        print(f"Inisde of b {n}")
        return a(n-1)
    
a(5)

print("---------------Head Recursion------------------")
def head_recursion(n: int):
    if n < 1:
        return n
    
    head_recursion(n-1)
    print(n)
    
head_recursion(5)
#last in first out

print("----------------Tail Recursion------------------")
def tail_recursion(n: int):
    if n < 1:
        return n
    print(n)
    return tail_recursion(n-1)

tail_recursion(5)



print("-----------------Stack Recursion----------------")
def a():
    print("1")
    b()
    print("2")
    
def b():
    print ("3")
    c()
    print ("4")

def c():
    print ("5")
    
a()