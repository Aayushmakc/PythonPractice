class Programmer:
  company="Microsoft"
  def __init__(self,name,salary,position):
    self.name=name
    self.salary=salary
    self.position=position

  def get_info(self):
    print(f"I am {self.name} currently working in {p.company} and My salary is {self.salary} as {self.position}")

p=Programmer("Aayushma",1000000,"Frontend Developer")
# # print(p.name,p.salary,p.position)
# p=Programmer()
p.get_info()