'''
a= "a very long string witj emails"
'''
# writing in file
st="Hi!!Aalu how are you"

f=open("myfile.text","w")
f.write(st)
f.close()



# Reading file
f=open("myfile.text","r")
text=f.read()
print(text)
f.close()