x=['a','b','c']
print(x)
dict_a = dict()
dict_a[x[0]]=[1,2,3]
x[0] = dict_a
print(x)