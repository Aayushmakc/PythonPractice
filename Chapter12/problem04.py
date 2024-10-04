class Calculator:
  def __init__(self,n):
    self.n=n

  def square(self):
    print(f"The square is {self.n*self.n}")

  def cube(self):
    print(f"The square is {self.n*self.n*self.n}")
 
  def squareroot(self):
    print(f"The squareroot is {self.n**0.5}")
  @staticmethod
  def greet():
    print("Helloo ALan")

  

  

ca=Calculator(6)
ca.square()
ca.cube()
ca.squareroot()
ca.greet()