class Employee:
  company="ITC"

  def show(self):
    print(f"The name is{self.name} and the salary is{self.salary}")

    

class Programmer(Employee):
  company="ITC Bhaktapur"
  def showLanguage(self):
      print(f"The name is{self.name} and the salary is{self.salary}")

a=Employee()
print(a.company)


b=Programmer()
print(b.company)
