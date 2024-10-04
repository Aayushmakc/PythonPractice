#A spam comment is defined as a text containing following keywords:"Make a lot money","buy now","Subscribe this","click this".Write a program to detect these spams
p1="Make a lot money"
p2="buy now"
p3="Subscribe this"
p4="click this"

message=input("Enter your comment:")
if((p1 in message) or(p2 in message)or (p3 in message) or(p4 in message)):
  print("This is a spam")

else:
  print("This is not a spam")