# print('i eat %s' %"aa") #format
# print('i eat {0} and {1}'.format('aaa','bbb'))
# name='ccc'
# age='ddd'
# print(f'i eat {name} and {age}')
# matrix1=[[1,2,3],[4,5,6],[7,8,9]]
# matrix2=[[1,2,3],[4,5,6],[7,8,9]]
# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.values())
# print('name' in a)
# s1=set([1,2,3,4,5,6])
# s2=set([4,5,6,7,8,9])
# print(s1|s2)
# b=a[:] #b=copy(a) 와 동치
# num=0
# prompt="1. Add\n2. Del\n3. List\n4. Quit"
# while num!=4:
#     print(prompt)
#     num=int(input())
# i=0
# while True:
#     print("Crtl+C %d" %i)
#     i=i+1
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=" ")
#     print("") #print는 디폴트값으로 줄바꿈이 세팅되어있다.
# a=[1,2,3,4]
# result=[num*3 for num in a] #리스트 컴프리헨션

# def add_many(*args):
#     result =0
#     for i in args:
#         result=result+i
#     return result
# print(add_many(1,2,3,4,5,6,7))

# def print_kword(**kv):
#     print(kv)
# print_kword(a=1,b=2,c='a')

# f='C:\\pydata\\json\\name.txt'

# print(f.replace("\\","/"))
# import sys
# args=sys.argv[1:]
# for i in args:
#     print(i)
a=['3','4','5']
f=open("C:/pydata/json/newfile.txt","w")
for i in a:
    f.write(i+"\n")
f.close
