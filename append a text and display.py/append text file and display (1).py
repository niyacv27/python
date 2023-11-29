file= open("file 3.txt","a+")
data=file.read()
file.write("This is a new line of text")
file=open("file 3.txt","r")
data=file.read()
print(data)







