f=open("poem.txt")
content=f.read()
if("twinkle" in content):
   print("twinkle is present in the content")
else:
   print("The word twinkle is not in the content")
f.close()