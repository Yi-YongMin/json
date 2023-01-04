import json
d = dict()
d['id'] = 1
d['name'] = 'pie'
d['hobby'] = ['game', 'tv', 'work']
d['test'] = True
file_path = 'C:\Users\82103\OneDrive - 인하대학교\바탕 화면\json'
with open(file_path, 'w', encoding='UTF-8') as fp:
    json.dump(d, fp)
