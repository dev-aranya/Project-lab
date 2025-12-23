#greater_number
# a1=int(input("Enter number a1 :"))
# a2=int(input("Enter number a2 :"))
# a3=int(input("Enter number a3 :"))
# a4=int(input("Enter number a4 :"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1 is greater",a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greater",a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("a3 is greater",a3)
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("a4 is greater",a4)


#pass_fail
# marks1=int(input("Enter marks1 = "))
# marks2=int(input("Enter marks2 = "))"
# marks3=int(input("Enter marks3 = "))

# total_percentage=(100*(marks1+marks2+marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed",total_percentage)
# else:
#     print("You are fail,try again nxt year",total_percentage)    


#include_word_sentence
# p1="Make a lot of money"
# p2="buy now "
# p3="subscribe this"
# p4="click this"

# message=input("enter your comment : ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is spam")
# else :
#     print("This comment is not spam")    


#user_name contains 10 charecters
# user_name=input("Enter name= ")

# if(len(user_name)<10):
#     print("Your name contains less than 10 cheracter")
# else:
#     print("All is well")    

#list or not
# li=["ovi","deb","nath","aranya","omi"]
# name=input("Enter your name : ")

# if(name in li):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")    


#grade
marks=int(input("Enter your marks : "))

if(marks<=100 and marks>=90):
    print("Ex")
elif(marks<=90 and marks>=80):
    print(" A")    
elif(marks<=80 and marks>=70):
    print(" B")    
elif(marks<=70 and marks>=60):
    print(" C")    
elif(marks<=60 and marks>=50):
    print("D ")    
elif(marks<=50 and marks>=40):
    print("E ")    
elif(marks<=40 and marks>=33):
    print(" E-")    
else:
    print("Fail")    