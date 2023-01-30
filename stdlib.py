# import datetime
# import time
# import shutil
# import glob
# day1=datetime.date(2021,4,26)
# day2=datetime.date(2023,1,30)
# diff=day2-day1
# print(diff.days)
# print(time.asctime(time.localtime(time.time())))
# print(time.ctime()) 
# #shutil.move("C:/pydata/json/name.txt","C:/pydata/jump_to_python_example/name.txt")
# print(glob.glob("C:/pydata/json/*")) # dt로 시작하는 파일들만 찾을때는 dt*로 작성.
# a="한글"
# b=a.encode('utf-8')
# print(b)
# print(type(b))
# class Mul:
#     def __init__(self, m):
#         self.m = m

#     def mul(self, n):
#         return self.m * n

# if __name__ == "__main__":
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3.mul(10))
#     print(mul5.mul(10)) 
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        print(word)
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))