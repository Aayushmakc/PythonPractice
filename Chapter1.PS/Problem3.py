import os
# select the directory whose content you want to list
directory_path = 'Python'

content=os.listdir(directory_path)
for item in content:
  print(item)