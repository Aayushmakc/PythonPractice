class Student:
  def __init__(self,phy,chem,math):
    self.phy=phy
    self.chem=chem
    self.math=math
    self.phy=phy
    

  @property
  def Calcpercentage(self):
   return str((self.phy+self.chem+self.math)/3) + "%"

stu=Student(23,45,67)
stu.phy=86

print(stu.Calcpercentage)