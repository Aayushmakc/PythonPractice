# write a python program to remove a given word from the list and ad strip it at the same Time

def rem(l,word):
   n=[]
   for item in l:
      if not(item==word):
         n.append(item.strip(word))
   return n
     
l=["Aayushma","Alan","anna","Aakriti","an"]
print(rem(l,"an"))