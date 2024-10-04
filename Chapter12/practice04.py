class Employee:
  language="Python"
  salary=1200000

  def __init__(self,name,language,salary ):#dunder method which is automatically called
    self.name=name
    self.language=language
    self.salary=salary
    print("I am creating a method")

  def getInfo(self):
    print(f"My name is {self.name}.The Language is {self.language}.The Salary is {self.salary}")

  def greet(self):
    print("Good Morning Alan!")

emp1=Employee("Aayushma","Javascript",1000000)
# emp1.language()
# emp1.salary()
emp1.getInfo()
emp1.greet()
# print("The language is",emp1.language)