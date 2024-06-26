import os
import shutil
try:
    path=input("Enter file path ")

    files=os.listdir(path)

    for i in files:
        name,extention= os.path.splitext(i)
        ext=extention[1:]
        folder_path=path+"\\"+ext
        if(os.path.exists(folder_path)):
            shutil.move(path+"\\"+i , path+"\\"+ext+"\\"+i)
        else:
            os.makedirs(folder_path)
            shutil.move(path+"\\"+i , path+"\\"+ext+"\\"+i)
except Exception as e:
    print("Wrong input Exception ",e)
        