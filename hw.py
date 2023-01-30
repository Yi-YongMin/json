# import os
# path='Y:/018_비식별화'
# lv0=os.listdir(path)
# f=open("C:/pydata/json/name.txt",'w')
# j=[]
# for i, item1 in enumerate(lv0):
#     lv00=os.listdir(path+'/'+item1)
#     for j, item2 in enumerate(lv00):
#         lv000=os.listdir(path+'/'+item1+'/'+item2)
#         for k, item3 in enumerate(lv000):
#             final=item1 +' '+item2+' '+item3+'\n'
#             f.write(final)
# import pandas as pd
# df=pd.read_csv('C:/pydata/json/name.txt',sep='\ ',encoding='utf-8')
# df.to_excel('level.xlsx',index=False)

import jump_to_python as jp
a=jp.FourCal(4,2)
print(a.add())
# for pathx, dirs, files in os.walk(path):
#     if files is True:
#         continue

#     pathx_split = pathx.replace('\\', '/').split('/')
    
#     if len(pathx_split) == 5:
#         print("level3")
#     elif len(pathx_split) == 4:
#         print("level2")
#     elif len(pathx_split) == 3:
#         print("level1")
#     else:
#         continue

# print(pathx)






# t=[]

# for k in range(len(lv00)):
#    t.append(str(lv0[0]+'/'+lv00[k]+'/'))




# lv00=os.listdir(path+'/'+lv0[0])


# for i in range(len(lv00))
# os.listdir(path+'/'+lv0[0]+'/'+lv00[0])
# lv000=os.listdir(path+'/'+lv0[0]+'/'+lv00[0])
# for i in lv000:
#     print(lv0[0]+' '+lv00[0]+' '+i)

# lv001=os.listdir(path+'/'+lv0[0]+'/'+lv00[1])
# for i in lv001:
#     print(lv0[0]+' '+lv00[1]+' '+i)

# lv002=os.listdir(path+'/'+lv0[0]+'/'+lv00[2])
# for i in lv002:
#     print(lv0[0]+' '+lv00[2]+' '+i)

            

# for k in range(len(lv00)):
#     j=j+(os.listdir(path+'/'+lv0[0]+'/'+lv00[k]))
#     for i in lv00[k]:
#         print((lv0[0]+' '+i))

#     for i in j:
#         print(lv0[0]+' '+lv00[0]+' '+i)
# t = []

# # for k in len(lv00):
# #     lv002=os.listdir(path+'/'+lv0[0]+'/'+lv00[k])
# #     lv3=[]
# #     for i in lv002:
# #         lv3=lv0[0]+' '+lv00[0]+' '+i
# #         print(lv3)
