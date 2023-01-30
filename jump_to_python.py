# f=open("C:/pydata/json/newfile.txt",'w')
# for i in range(1,11):
#     data="%d번째 줄 입니다. \n" %i
#     f.write(data)
# f.close()
# f=open("C:/pydata/json/newfile.txt",'r')
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         break
# f.close()
#readlines 는 리스트로 readline들을 저장.
# while True:
#     data=input()
#     if not data:
#         break
# f=open("C:/pydata/json/newfile.txt",'r')
# for line in f:
#     print(line)
# print(f)
# f.close()
# with open("C:/pydata/json/newfile.txt",'r') as f:
#     line=f.readlines()
#     print(line)
class FourCal:
    def __init__(self, first, second):#외워둬야 함. setdata와 똑같이 쓰지만 얘는 객체가 생성될 때 자동적으로 호출된다.
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result
    
class SafeFourCal(FourCal):
        def div(self):
            if self.second==0:
                return 0
            else:
                result = self.first / self.second
                return result
    
# a=MoreFourCal(4,2)
# print(a.pow())
# b=SafeFourCal(4,0)
# print(b.div())
# class Family:
#     lastname="lee"
# a=Family()
# b=Family()
# a.lastname="choi"
# print(a.lastname)
# print(b.lastname)

import sys
print(sys.path)