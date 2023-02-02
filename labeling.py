import glob
import shutil
import os

# img_path = '/home/visionin_rnd/TS_FOLDER/YOLO/20221101_185719_nan_santafe/image/front'
# img_files = glob.glob(os.path.join(img_path,'*.jpg'))
img_path = 'X:\\해상 객체 이미지\\Validation\\sample1000\\SEG'
img_files = glob.glob(os.path.join(img_path,'장항*.jpg'))
# print("img",img_files)
json_path = 'X:\\해상 객체 이미지\\Validation\\[라벨]서해_장항_1구역_SEG'
# for (root, directories, jsonfiles) in os.walk(json_path):
#     for jsonfile in jsonfiles:
#         if '.json' in jsonfile:
#             file_path = os.path.join(root, jsonfile)
#             print(file_path)
# print("TXTFILE", json_files)

# for (root, directories, jsonfiles) in os.walk(json_path):
# 	for jsonfile in jsonfiles:
# 		if '.json' in jsonfile:
# 			file_path = os.path.join(root, jsonfile)
# 			json_name = os.path.splitext(os.path.basename(file_path))[0]
			# print("jsonmmm",file_path)

# img copy
for img_file in img_files:
	img_name = os.path.splitext(os.path.basename(img_file))[0]
	img_name_dot = img_name + '.'
	print("img_name_dot",img_name_dot)
	for (root, directories, jsonfiles) in os.walk(json_path):
		for jsonfile in jsonfiles:
			if '.json' in jsonfile:
				file_path = os.path.join(root, jsonfile)
				if file_path.find(img_name_dot) != -1:
					try:
						print("same_file_path", file_path)
						shutil.copy(file_path, (img_file.replace(".jpg", ".json")))
					except:
						pass
# for img_file in img_files:
# 	img_name = os.path.splitext(os.path.basename(img_file))[0]
# 	img_name_dot = img_name+'.'
# 	for (root, directories, jsonfiles) in os.walk(json_path):
# 		for jsonfile in jsonfiles:
# 			if '.json' in jsonfile:
# 				file_path = os.path.join(root, jsonfile)
# 				# print("json_file", file_path)
# 				json_name =os.path.splitext(os.path.basename(file_path))[0]
# 				# print("js",json_name)
# 				if file_path.find(img_name_dot) != -1:
# 					try:
# 						print("same_file_path", file_path)
# 						shutil.copy(file_path, (img_file.replace(".jpg", ".json")))
# 					except:
# 						pass

	# for json_file in json_files:
	# 	if json_file.find(img_name) != -1:
	# 		print("json_file",json_file)
			# try:
			# 	shutil.copy(json_file, (img_file.replace(".jpg", ".json")))
			# 	print('sss',img_file.replace(".jpg", ".json"))
			# except:
			# 	pass
