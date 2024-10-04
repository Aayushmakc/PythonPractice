 #indentation is important used to indent meaning you are inside the loop
#if elif and else are connected
a = int(input("Enter your age: ")) 

if a >= 18:  
   print("You are above the age of consent")
   print("Good for you")

elif(a<0):
    print("You are entering an invalid age")
    
elif(a==0):
    print("You are entering 0 which is not valid")

else:
    print("You are below the age of consent")

print("End of program")  
