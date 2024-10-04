# create student class that takes name & marks of 3 subjects as argument in constructor.Then create a method to print the average

class Student:
  def __init__(self,name,marks): 
    self.name=name
    self.marks=marks

  def get_avg(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("Hi",self.name ,"your average score is :" ,sum/3)

s1 = Student("Aayushma",[99,90,98])
s1.get_avg()
# print(s1.name,s1.marks)
# s1.get_avg()