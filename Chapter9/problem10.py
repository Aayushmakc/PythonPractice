# WAP a program to print multiplication table of n using for loops in revered order
n=int(input("Enter the number:"))
for i in range(1,11):
  print(f"{n}*{11-i}={n*(11-i)}")
  i+=1