# create a 2D vector and create another class representing a 3-Dvector
class TwoDVector:
  def __init__(self,i,j):
    self.i=i
    self.j=j
  def Show(self):
    print(f"The two vectors are {self.i}i+{self.j}j ")

class ThreeDVector(TwoDVector):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k=k

  def Show(self):
    print(f"The two vectors are {self.i}i + {self.j}j +{self.k}k")


a=TwoDVector(1,3)
a.Show()

b=ThreeDVector(2,3,4)
b.Show()