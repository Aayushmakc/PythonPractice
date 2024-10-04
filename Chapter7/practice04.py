s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
# Output must be 3 but it gives two because two numbers are same that is 20 and 20.0
s={}    #type is dictionary
print(type(s))