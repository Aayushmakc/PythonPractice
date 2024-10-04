a=89#global


def func():
  global a   #yesari global banauna ni milxa
  a=43#local
  print(a)


print(a) #function call bhax aina so initial value nai lina
func() #function call bhayo
print(a)#aba global vallue chnage bhayo