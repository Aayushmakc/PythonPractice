#Methods of dictionary
#Dictionary is the collection of key value pair
#a=[key,value]
# .items
marks={
 "Aayushma":200,
  "Alan":100,
  "Aakriti":400,
  0:"Abhishek"



}
print(marks["Aayushma"])
#list of list is allowed in python
print(marks.items())

# .keys .... lest side is a key
print(marks.keys())

#.values.......right side is a value
print(marks.values())

#update the value of current items plus it also add new items
marks.update({"Alan":500,"Renuka":80})
print(marks)

# getmethod
print(marks.get("Aayushma"))#Prints none
print(marks["Aayushma"])#returns error
 #pop method
value=marks.pop("Aayushma")
print(value)
#popitem method
item=marks.popitem()