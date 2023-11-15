a=input("Enter a name:")
if a.endswith("ing"):
    string = a+"ly"
    print (string)
elif a.endswith("ly"):
    string=a+"ing"
    print(string)
else:
    print("No change")
