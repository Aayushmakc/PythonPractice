
#input function ko output chai string hunxa so that it needs to be typecasted that's why we use int before input for numbers

a1=int(input("Enter the number 1:")) #shift alt downwardarrow
a2=int(input("Enter the number 2:"))
a3=int(input("Enter the number 3:"))
a4=int(input("Enter the number 4:"))

if(a1>a2 and a1>a3 and a1>a4):
  print("Greatest number is a1:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
  print("The Greatest number is a2",a2)

elif(a3>a1 and a3>a2 and a3>a4):
 print("The Greatest number is a3",a3)

else:
  print("The Greatest number is a4",a4)


print("Great Job and Happy coding!!!!")