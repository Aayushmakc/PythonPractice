from functools import reduce
l=[33,45,666,1,2,34]

def max(a,b):
  if(a>b):
    return a
  return b

print(reduce(max,l))
