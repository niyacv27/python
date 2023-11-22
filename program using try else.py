a=int(input("Enter a first  number:"))
b=int(input("Enter second number:"))
try:
    c=a/b
    print("Result:",c)
except:
        print("cannot be divisible by zero")
else:
        print("successfully completed")
