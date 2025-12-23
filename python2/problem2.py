# name=input("Enter your name : ")
# print("Good morning",name)
# print(f"Good morning, {name}")

#replace string
letter=''' Dear <|name|> ,
you are selected!
<|date|>'''
print(letter.replace("<|name|>","Ovi").replace("<|date|>","24 August,2025"))