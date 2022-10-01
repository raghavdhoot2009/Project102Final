import os
import shutil
from distutils import extension
from genericpath import exists

from_dir =  "C:\\Users\\Raghav\\Downloads"
to_dir = "C:\\Users\\Raghav\\Desktop\\Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files :
  name,extension =  os.path.splitext(file)
  print(name)
  print(extension)

  if extension=='':
    continue
  
  if extension in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = from_dir + '/' + file
    path2 = to_dir + '/' + "Text_files"
    path3 = to_dir + '/' + "Text_files" + '/' +  file
 
  if os.path.exists(path2):
   print ("Moving" + file + ".....")
  
   shutil.move(path1,path3)
  else :
   os.makedirs(path2)
   print ("Moving" + file + ".....")

   shutil.move(path1,path3)