# Create a class with a class attribute a;create an object from it and set "a" directly using object.a=o.Does this change the class attribute

class Demo():
  a=4
o=Demo()
print(o.a) #print class attribute because instance attribute is not present
o.a=0
print(o.a) #prints instance attribute because instance attribute is present
print(Demo.a) #prints the class attribute