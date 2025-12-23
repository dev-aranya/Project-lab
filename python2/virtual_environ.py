#lambda function use
# square=lambda x:x*x
# print(square(6))

#join
# a=["Ovi","Aranya","Deb","Nath"]
# final=" :: ".join(a)
# print(final)

#formet
# a="{} is a good {}".format("Ovi","boy")
# print(a)

#map,filter,reduce
# l=[1,2,3,4,5,6]
# square= lambda x:x*x
# sqlist=map(square,l)
# print(list(sqlist))

# def even(n):
#     if(n%2==0):
#         return True
#     return False
# onlyeven=filter(even,l)
# print(list(onlyeven))


#multiplecation table
# table=[str (8*i) for i in range (1,11)]
# s='\n' .join(table)
# print(s)

#divisible by 5
# def divisible5(n):
#     if(n%5==0):
#         return True
#     return False

# a=[1,222,3444,566,25,67,8899]
# f=list(filter(divisible5,a))
# print(f)


#list greater
from functools import reduce
l=[12,34,56,34,5667,7887,65]

def greater(a,b):
    if(a>b):
        return a
    return b 
print(reduce(greater,l))
