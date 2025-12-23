class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language="python"
    def printlanguages(self):
        print(f" Out of all language here in your language : {self.language}")        

class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")  

a=Employee()
b=Programmer()        

b.show()
b.printlanguages()
b.showlanguage()