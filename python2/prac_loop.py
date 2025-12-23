#multiplecation table
# n=int(input("Enter number = "))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

#greet in list
# l=["ovi","shuvo","shohag","Omi"]
# for name in l:
#     if(name.startswith("s")):
#         print(f"Hello {name}")

#multiplecation table
# n=int(input("Enter number = "))
# i=1
# while(i<11):
#     print(f"{n}*{i}={n*i}")   
#     i+=1     


#prime number
# n=int(input("Enter number : "))
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime")
#         break
# else:
#      print("Number is prime ")

#sum
# n=int(input("Enter number : "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

#factorial
# n=int(input("Enter num : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"the factorial of {n} is {fact}")

# triangle star pattren
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1),end=" ")
#     print("")

#right angle triangle pattern
# n=int(input("Enter number : "))
# for i in range(1,n+1):
#     print("* "*i,end=" ")
#     print("")
        
#polygon pattern
# n=int(input("Enter any number : "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print(" ")    

#multiplecation table
n=int(input("Enter any number : "))
for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")