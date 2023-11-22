try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print("a/b=%d"%c)
except Exception:
    print("can't divide by zero")
    print(Exception)
else:
    print("Hi iam else block")
