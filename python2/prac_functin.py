#greatest number
# a=int(input("Enter number : "))
# b=int(input("Enter number : "))
# c=int(input("Enter number : "))
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
    
  
# print(greatest(a,b,c))    

#convert temperature
# f=int(input("Enter temperature F : "))
# c=5*(f-32)/9
# print(c)

# def f_to_c(f):
#     return 5*(f-32)/9
# f=int(input("Enter temp in f: "))
# # print(f_to_c(f))
# c=f_to_c(f)
# print(f"{round(c,2)} °c")

#avoid new line
# print("a")
# print("b")
# print("c",end="")
# print("a",end="")

#recursion
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(6))
# print(sum(8))

#pattern 
# def pattern(n):
#     if(n==0):
#         return 
#     print("*"* n)
#     pattern(n-1)
# pattern(6)        

# convert inch to centimeter
# def inch_to_cms(inch):
#     return inch * 2.54
# n=int(input("Enter inch  : "))
# print(f"The corresponding value in cms is {inch_to_cms(n)}")

#remove list iteam
# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l
# l=["Ovi","Aranya","deb"]
# print(rem(l,"Ovi"))    
# print(rem(l,"deb"))    

#multiplecation
def multiply (n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i} ")
print(multiply(5))        

    