# BY USING THIS CODE WE HAVE TO RENAME OUR FILES IN A FOLDER AUTOMATICALLY WITHIN A SECONDS

import os
def renamer():
    i = 0
    path = "C:\\Users\\Anmol Agarwal\\Desktop\\New folder\\img\\"
    for filename in os.listdir(path):
        name=f"images.{i}.jpg"
        src = path + filename
        dest = path + name

    path = "C:\\Users\\Anmol Agarwal\\Desktop\\New folder\\songs\\"
    for filename in os.listdir(path):
        name=f"songs.{i}.mp3"
        src = path + filename
        dest = path + name

    path = "C:\\Users\\Anmol Agarwal\\Desktop\\New folder\\files\\"
    for filename in os.listdir(path):
        name=f"files.{i}.pdf"
        src = path + filename
        dest = path + name        

        os.rename(src,dest)
        i = i+1
if __name__=="__main__":
    renamer()