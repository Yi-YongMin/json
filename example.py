import json
d = dict()
d['id'] = 1
d['name'] = 'pie'
d['hobby'] = ['game', 'tv', 'work']
d['test'] = True
file_path='C:\pydata\json\dictd.json'
with open(file_path, 'w',encoding='UTF-8') as fp:
    json.dump(d,fp,indent=4)

