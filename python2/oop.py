#class.py

# class Employee:
#     name="ovi"
#     language="Python"
#     salary=2300000
    
# ovi=Employee()
# print(ovi.name,ovi.language)

# aranya=Employee()
# aranya.name="dj"
# aranya.language="Java"
# print(aranya.name,aranya.salary,aranya.language)


#Self.py

# class Employee:
#     name="ovi"
#     language="Python"
#     salary=2300000
#     def getinfo(self):
#               print(f"The languaage is {self.language}.The salary is {self.salary}")

#    #@staticmethod
     #def greet():
#     def greet(self):
#             print("Good morning")
    
# ovi=Employee()
# ovi.greet()
# ovi.getinfo()


#constructor
class Employee:
    name="ovi"
    language="Python"
    salary=2300000

    def __init__(self,name,salary,language):
           self.name=name
           self.salary=salary
           self.language=language
           print("I am creating an object")
    def getinfo(self):
              print(f"The languaage is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
            print("Good morning")
    
ovi=Employee("Aranya",250000,"java script")
print(ovi.name,ovi.salary,ovi.language)