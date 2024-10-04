# class Number:
#   def __init__(self,n):
#     self.n=n

#   def add(self,num):
#     return self.n+ num.n

# n=Number(1)
# m=Number(2)
# print(n+m)


# print(1+2)
# print(type(1))
# print("Aayushma"+"kc")
# print([1,2,3]+[4,5,6])
# print(type("Aayushma"))
# print(type([1,2,3]))

class Complex:
  def __init__(self,real,img):
    self.real=real
    self.img=img

  def showNumber(self):
    print(self.real,"i +",self.img,"j")

  def __add__(self,num2):#dunder
    newReal=self.real+num2.real
    newImg=self.img+ num2.img
    return Complex(newReal,newImg)

  def __sub__(self,num2):#dunder
    newReal=self.real-num2.real
    newImg=self.img- num2.img
    return Complex(newReal,newImg)
    
    

num1=Complex(1,2)
num1.showNumber()

num2=Complex(3,4)
num2.showNumber()

# num3=num1.add(num2)
# num3.showNumber()
num3= num1+num2
num3.showNumber()

num4=num2-num1
num4.showNumber()







