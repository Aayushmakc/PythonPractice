class Employee:
  def __init__(self):
    print("I am learning inheritance in python")
  a=1

class Programmer(Employee):
   def __init__(self):
    print("I am learning  in python")
   b=4

class Coder(Programmer):
   def __init__(self):
    super().__init__()
    print("I am trying to learn python")
   c=3


# p=Employee()
# q=Programmer()
r=Coder()
# print(p.a)
# print(q.a,q.b)
print(r.a,r.b,r.c)