# search twinkle word
# poem=open("poem.txt")
# content=poem.read()
# if("Twinkle" in content):
#     print("The word twinkle is present in the content")
# else:
#     print("The word twinkle is not present in the content")
# poem.close()        


#game
# import random

# def game():
#     print("You are playing the game")
#     score=random.randint(1,60)
#     #Fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0    
#     print(f"your score {score}")
#     if(score>hiscore):
#         #write this hiscore to the file
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()        


#Table file generate
# def generatetable(n):
#     table=""
#     for i in range(1,11):
#         table += f"{n}*{i} ={n*i}\n"
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)

# for i in range (2,21):
#     generatetable(i)        


#word dunkey replace
# word="Donkey"

# with open ("new.txt","r") as f:
#     content=f.read()
# contentnew=content.replace(word,"######")    
# with open ("new.txt","w") as f:
#     f.write(contentnew)


#copy file
# with open ("this.txt") as f:
#     content=f.read()
# with open("this_cpy.txt","w") as f:
#     f.write(content)    

#same file identical
# with open("this.txt") as f:
#     content1=f.read()
# with open("this_cpy.txt") as f:
#     content2=f.read()
# if(content1==content2):
#     print("Yes these file are identical")
# else:
#     print("No these file are identical")      
     

#hide file
# with open("this_cpy.txt","w") as f:
#     f.write("")


#Rename
with open ("old.txt") as f:
    content=f.read()

with open ("rename_old.txt","w") as f:
    f.write(content)    