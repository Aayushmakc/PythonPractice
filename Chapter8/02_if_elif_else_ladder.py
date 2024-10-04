a = int(input("Enter your age: ")) 

#If elif else ladder
if(a%2==0):
    print("The number you entered is even")

#end of if statement number 1
#if can be alone but else  and elif cannot be alone
if a >= 18:  
   print("You are above the age of consent")
   print("Good for you")

elif(a<0):
    print("You are entering an invalid age")
    
elif(a==0):
    print("You are entering 0 which is not valid")

else:
    print("You are below the age of consent")
    
#end of if statement number 1

print("End of program")  
