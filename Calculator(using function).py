def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
a=int(input("Enter the first  number:"))
b=int(input("Enter the second number:"))
print("\nOptions\n1.Adition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Adittion =", (add(a,b)))
elif choice==2:
     print("Subtraction =", (subtract(a,b)))
elif choice==3:
     print("Multiplication =", (multiply(a,b)))
elif choice==4:
     print("Division =", (division(a,b)))
else:
    print("Invalid")
