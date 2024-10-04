class Employee:
  language="Python"
  salary=1200000


  def getInfo(self):
    print(f"The Language is {self.language}.The Salary is {self.salary}")
  @staticmethod # can be done without passing object self
  def greet():
    print("Good Morning Alan!")

emp1=Employee()
# emp1.language()
# emp1.salary()
emp1.getInfo()
emp1.greet()
# print("The language is",emp1.language)