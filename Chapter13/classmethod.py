class Employee:
  d=1
  @classmethod
  def show(cls):
    print(f"The class value of d is {cls.d}")



a=Employee()
a.d=30  #instance value ko priority badi hunxa
a.show()