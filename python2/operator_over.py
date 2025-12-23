class Number:
    def __init__(self,n):
        self.n=n


    def __add__(self,b):
        return self.n + b.n
    
n=Number(3)
m=Number(3)
print(n+m)