# Can you change the self to slf

# to make the readabilty we use self instead of self we can use anything

import random
class Train:


  def __init__(slf,trainNo):
   slf.trainNo=trainNo
  
   
  


  def book(slf,fro,to):
    print(f"Ticket is booked in train no:{slf.trainNo} from {fro} to {to}")

   
  def getstatus(slf):
     print(f"The train no {slf.trainNo} is running successfully")

  def getfare(slf,fro,to):
    print(f"The Trainfare in train no:{slf.trainNo} from {fro} to {to} is {random.randint(1,555)}")

t=Train(333)
t.book("Kathmandu","Bhaktapur") 
t.getstatus()
t.getfare("Kathmandu","Bhaktapur")