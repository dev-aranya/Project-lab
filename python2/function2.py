# def avg():
#     a=int(input("Enter 1st number : "))
#     b=int(input("Enter 2nd number : "))
#     c=int(input("Enter 3rd number : "))
#     average=(a+b+c)/3
#     print(average)

# avg()
# avg()

# def good(name):
#     print("good bye," + name)
# good("Ovi")    
# good("Aranya")    
# good("Deb")    
    
# def goodday(name,ending="Thank you"):
#     print(f"Good day ,{name}")
#     print(ending)
# goodday("ovi")
# goodday("Aranya" ,"Thanks")

#Recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("Enter any number : "))
print(f"The factorial of this number is : {factorial(n)}")