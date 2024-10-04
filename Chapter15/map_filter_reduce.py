# map applies function to every element
from functools import reduce
#Map Example
l=[1,2,3,4,5,6]
square = lambda x:x*x
squaredlist=map(square,l)
print(list(squaredlist))


#Filter Example

def even(n):
  if(n % 2 ==0):
    return True
  return False

onlyEven =filter(even,l)
print(list(onlyEven))


#Reduce Example
def sum(a,b):
  return a+b
print(reduce(sum,l))

mul =lambda x,y:x*y
print(reduce(mul,l))

