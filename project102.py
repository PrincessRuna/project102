import os
import shutil 

from_dir = "C:/Users/Shinj_28/Downloads"
to_dir="C:/Users/Shinj_28/Downloads/documentFiles" 

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1= from_dir + '/' + filename
        path2= to_dir + '/' + "documentFiles"
        path3= to_dir + '/' + "documentFiles" + '/' + filename
        
        if os.path.exists(path2):
            print("moving" + filename + "..." )
            shutil.move (path1,path3)
        else :
            os.makedirs(path2)
            print("moving" + filename + "..." )
            shutil.move (path1,path3)