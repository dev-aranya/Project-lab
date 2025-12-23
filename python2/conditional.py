a=int(input("Enter your age : "))

if(a%2==0):
    print("A is even")

if(a>18):
    print("You are adult")
    print("Good for you")

elif(a<0):
    print("your are entering invalid age")  
elif(a==0):
    print("you entering 0 which is invalid age ")      

else :
    print("You are not adult")    

print("End programm")