import os
import glob
path='Y:/018_비식별화'
filelv1=[]
filelv3=[]
for file1 in os.listdir(path):
    filelv1.append(file1)

filelv1_0=(glob.glob('Y:/018_비식별화'+"/"+filelv1[0]+"/*"))
filelv1_1=(glob.glob('Y:/018_비식별화'+"/"+filelv1[1]+"/*"))
filelv1_2=(glob.glob('Y:/018_비식별화'+"/"+filelv1[2]+"/*"))
filelv1_3=(glob.glob('Y:/018_비식별화'+"/"+filelv1[3]+"/*"))
filelv1_4=(glob.glob('Y:/018_비식별화'+"/"+filelv1[4]+"/*"))
filelv1_5=(glob.glob('Y:/018_비식별화'+"/"+filelv1[5]+"/*"))
for i in filelv1_0:
    filelv3.append(glob.glob(i+"/*"))
for i in filelv1_1:
    filelv3.append(glob.glob(i+"/*"))
for i in filelv1_2:
    filelv3.append(glob.glob(i+"/*"))
for i in filelv1_3:
    filelv3.append(glob.glob(i+"/*"))
for i in filelv1_4:
    filelv3.append(glob.glob(i+"/*"))
for i in filelv1_5:
    filelv3.append(glob.glob(i+"/*"))

final=[]

for i in filelv3:
    for j in i:
        final.append(j.replace("Y:/018_비식별화","").replace("\\","/").replace("/"," ").lstrip())
f=open("C:/pydata/json/final.txt","w")

for k in final:
    f.write(k)
    f.write("\n")
f.close
