import random
class Train:


  def __init__(self,trainNo):
   self.trainNo=trainNo
  
   
  


  def book(self,fro,to):
    print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

   
  def getstatus(self):
     print(f"The train no {self.trainNo} is running successfully")

  def getfare(self,fro,to):
    print(f"The Trainfare in train no:{self.trainNo} from {fro} to {to} is {random.randint(1,555)}")

t=Train(333)
t.book("Kathmandu","Bhaktapur") 
t.getstatus()
t.getfare("Kathmandu","Bhaktapur")