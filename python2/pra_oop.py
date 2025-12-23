#two D,three D vector
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f" The vector is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f" The vector is {self.i}i + {self.j}j + {self.k}k")

# a=TwoDVector(3,4)
# a.show()

# b=ThreeDVector(5,3,9)
# b.show()


#pet animal
# class animals:
#    pass
# class pets(animals):
#    pass
# class Dog(pets):
#    @staticmethod
#    def bark():
#       print("BOW Bow")

# d=Dog()
# d.bark()      


#Employee - salalry
# class Employee:
#     salary=222
#     increment=20
#     @property
#     def salaryafterincrement(self):
#       return(self.salary + self.salary *(self.increment/100))
    
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#        self.incriment=((salary/self.salary) -1) *100
    
# e=Employee()
# print(e.salaryafterincrement)    
# e.salaryafterincrement=270
# print(e.increment)

#complex number
# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i

#     def __add__(self,c2):
#         return Complex(self.r + c2.r,self.i + c2.i)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1=Complex(1,2)    
# c2=Complex(2,3) 
# print(c1 + c2)  

#vector
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __add__(self,other):
        result=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f" Vector{self.x},{self.y},{self.z}" 

v1=Vector(1,3,4)       
v2=Vector(2,5,9)       
v3=Vector(8,2,4)       


print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)



