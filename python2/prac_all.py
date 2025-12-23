#nth position print
# l=[1,2,3,4,5,6,7,8]
# for i, item in enumerate(l):
#     if i ==2 or i==4 or i==6:
#         print(item)


#multiplecation table
# n=int(input("Enter a number : "))
# table=[n*i for i in range(1,11)]
# print(table)


#try function
# try:
#     a=int(input("enter any num : "))
#     b=int(input("enter any num : "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infinite")    

#table
n=int(input("Enter num : "))
table=[n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(table) + "\n")
