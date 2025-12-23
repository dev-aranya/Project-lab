#programmer microsoft
# class Programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,pin):
#            self.name=name
#            self.salary=salary
#            self.pin=pin

# p=Programmer("Ovi",127889,"43tty")
# print(p.name,p.salary,p.pin ,p.company)
# a=Programmer("Omi",125679,"4hu5y")
# print(a.name,a.salary,a.pin ,a.company)
        

#calculator
# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube (self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")

# a=Calculator(5)
# a.square()
# a.cube()
# a.squareroot()

#create  class attribute
# class Demo:
#     a=4
# o=Demo()
# print(o.a)
# o.a=5
# print(o.a)   
# print(Demo.a) 

#staticmethod
# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube (self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")
#     @staticmethod
#     def hello():
#         print("Hello There !")    


# a=Calculator(5)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()


#book train ticket
# from random import randint
# class Train:
#     def __init__(self,trainNo):
#         self.trainNo=trainNo
#     def book(self,fro,to):
#         print(f"Train in booked i train no:{self.trainNo} from {fro} to{to}")
#     def getstatus(self):
#         print(f"Train no:{self.trainNo} is running on time")
#     def getfare(self,fro,to):
#         print(f"Ticket fare in train no:{self.trainNo} from{fro} to {to} is {randint(222,5555)}")

# t=Train(43125) 
# t.book("jessore","Dhaka")
# t.getstatus()
# t.getfare("jessore","Dhaka")       


#change self parameter
from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(self,fro,to):
        print(f"Train in booked i train no:{self.trainNo} from {fro} to{to}")
    def getstatus(self):
        print(f"Train no:{self.trainNo} is running on time")
    def getfare(self,fro,to):
        print(f"Ticket fare in train no:{self.trainNo} from{fro} to {to} is {randint(222,5555)}")

t=Train(43125) 
t.book("jessore","Dhaka")
t.getstatus()
t.getfare("jessore","Dhaka") 
