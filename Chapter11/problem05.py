# from a file containing numbers seperated by comma,print the count of even numbers
count=0
with open("myfile.text","r") as f:
  data=f.read()
  print(data)
  nums=data.split(",")
  for val in nums:
    if(int(val)%2 == 0):
      count +=1
print(count)