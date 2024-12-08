

# Online Python - IDE, Editor, Compiler, Interpreter

def factorial(n):
    if(n == 0):
        return 1
    elif n == 1:
        return 1
    
    else:
        return n*factorial(n-1)
        
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=6
print("Factorial of ", num , " is ", factorial(num))
print("fibonacci num at ", num ," is ", fibonacci(num))
