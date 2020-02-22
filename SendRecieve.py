#send file####################################################################################
import os,sys
from  zipfile import ZipFile
count_file = math.ceil(os.stat('146.avi').st_size /(1024*1024*99))
with open('146.avi','rb') as avi:
    for i in range(count_file):
        zipfile = f'file{i}.zip'
        file = f'file{i}.txt'
        with ZipFile(zipfile, 'w') as myzip:
            with open(file,'wb') as temp:
                temp.write(avi.read(99*1024*1024))
            myzip.write(file)
            os.remove(file)
#get file####################################################################################
import os,sys,glob
from  zipfile import ZipFile
file_names = [x for x in sorted(glob.glob('*.zip'), key=os.path.getmtime) if 'file' in x]
with open('film.avi','wb') as file:
    for i in file_names:
        with ZipFile(i, 'r') as myzip:
            myzip.extractall()
            with open(myzip.namelist()[0],'rb') as file2:
                file.write(file2.read())
            os.remove(myzip.namelist()[0])
