

#1.user Input and Replace String Template “Hello <<UserName>>, How are you?” 

temp="Hello <<UserName>>, How are you?"
name=input("Enter username\n")
temp=temp.replace("<<UserName>>",name)
print(temp)
