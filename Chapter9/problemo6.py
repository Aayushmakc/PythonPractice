n=int(input("Enter the number:"))

# using for loop
# fact=1
# for i in range(1,n+1):
#   fact=fact*i
# print(f"The factorial of {n} is {fact}")

# using while loop
fact=1
i=1
while(i<=n):
  fact=fact*i
  i+=1

print(f"The factorial of {n} is{fact}")