class Employee:
  company="ITC"

  def show(self):
    
    print(f"The name is {self.company} and the salary is {self.company}")

class Coder:
   language="Python"  
   def printLang(self)  :
      print(f"Out of all language you language is : {self.language}")

class Programmer(Employee,Coder):
  company="ITC Bhaktapur"
  def showLanguage(self):
      print(f"The name is {self.company} and the language is {self.language}")

a=Employee()



b=Programmer()
b.show()
b.printLang()
b.showLanguage()

