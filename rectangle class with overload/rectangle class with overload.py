#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Rect:
    def __init__(self, a, b):
        self.length = a
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

h1 = int(input("Enter length of the first rectangle: "))
b1 = int(input("Enter breadth of the first rectangle: "))
h2 = int(input("Enter length of the second rectangle: "))
b2 = int(input("Enter breadth of the second rectangle: "))

rect1 = Rect(h1, b1)
rect2 = Rect(h2, b2)

if rect1 < rect2:
    print("Rectangle 2 is greater than Rectangle 1")
else:
    print("Rectangle 1 is greater than Rectangle 2")

