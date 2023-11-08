a=int(input("Enter a number:"))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
c=factorial(a)
print("Factorial of "+str(a)+ " is:",c)
