# del keyword
class Student:
  def __init__(self,name):
    self.name=name

s1=Student("Aayushma")
del s1
print(s1.name)