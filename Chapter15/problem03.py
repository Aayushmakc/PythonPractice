# A list contains the multiplication table of 7.write a program to convert it to verticl string of same number

table=[str(7*i) for i in range(1,11)]
s= "\n".join(table)
print(s)