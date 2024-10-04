# Create a class Employee and add Salary and increment property to it

class Employee:
    salary = 7000
    increment = 80

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100
     

e = Employee()
e.salaryAfterIncrement=10
print(e.increment)
