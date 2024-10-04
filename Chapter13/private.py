# class Employee:
#   def __init__(self,acc_name,acc_no):
#     self.acc_name=acc_name
#     self.__acc_no=acc_no

#   def reset(self):
#     print(self.__acc_no)

# Em=Employee("fixed",1223455555)
# print(Em.acc_name)
# Em.reset()


class Person:
  __name="Anonymous"#private attribute


  def __hello(self):
    print("Hello Aayushma!")

  def welcome(self):
    self.__hello()
  

p1=Person()
# print(p1.welcome())
p1.welcome()