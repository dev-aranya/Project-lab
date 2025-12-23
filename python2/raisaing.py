a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

if(b==0):
    raise ZeroDivisionError(" Hey our program is not meant to devide numbers by zero")
print(f"The division a/b is {a/b}")