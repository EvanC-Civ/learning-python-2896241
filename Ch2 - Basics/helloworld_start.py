#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

name="j'osh, Josh.!"
name=name.lower()
print(name)
punct = [" ", ",", "'", ".", "!", "?"]
i=0
while not(name.isalpha()):
    name=name.replace(punct[i],"")
    i+=1

print(name)
namerev=name[::-1]
# flag=True
# #flag1 = True if name==namerev else False
# #print("first chack",name==namerev)

# for x in range(len(name)):
#     #print(x)
#     if name[x]!=namerev[x]:
#         flag=False
#         break
# print(flag)