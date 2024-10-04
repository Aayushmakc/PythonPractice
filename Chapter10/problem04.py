# WAp a program to fins the sum of n natural number
def sum(n):
  if(n==1):
    return 1
  return sum(n-1)+n

a=int(input("Enter the natural number:"))
print(f"The sum of the natural number is:",sum(a))
  

