x=int(input("Enter first number"))
y=int(input("Enter second number"))
print("\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
ch=int(input("Enter the choice:"))
if(ch==1):
    c=x+y
    print("sum=",c)
elif(ch==2):
    c=x-y
    print("Substraction=",c)
elif(ch==3):
    c=x*y
    print("Multiplication=",c)
elif(ch==4):
    c=x/y
    print("Division=",c)
else:
    print("invalid")
