class student:
 #default constructors
#  def __init__(self):
#    pass

  #parameterized constructors
  def __init__(self,name,marks):
    print("creating new student in Database..")
    self.name=name
    self.marks=marks
    
  def hello(self):
    print("Hello students",self.name)   
  def get_marks(self):
    return self.marks
 

s1=student("Alan",100)
print(s1.name ,s1.marks)

s2=student("Aayushma",200)
print(s2.name,s2.marks)

s1.hello()
print(s1.get_marks())