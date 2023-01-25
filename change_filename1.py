import os
import glob
import shutil


# file_list = glob.glob(f"/home/vis-35/TS_FOLDER/OpenPCDet/*test*/kitti_label/*.txt", recursive=True)
# file_list = glob.glob(f"/home/vis-35/TS_FOLDER/OpenPCDet/day_sunny_highway_20220803_142736_santafe/velo/*.bin", recursive=True)
# file_list = glob.glob(f"/home/vis-35/TS_FOLDER/OpenPCDet/new_data/kitti_1107/sunset_cloudy_normal_20220803_094139_santafe/bin/*.bin", recursive=True)
file_list = glob.glob(f"/home/vis-35/SYNCRO_NAS/1205OpenPCDet/gumsu_ori_data/kitti/training/day_sunny_normal_20220901/velodyne_orig/*.bin", recursive=True)
# print("file_list",file_list)
for file_path in file_list:
    # print(file_path)
    split_list = file_path.split("/")
    # folder = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+split_list[5]+"/"+split_list[6]+"/"
    # copyfolder = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+"new_data"+"/"+"kitti"+"/"+"velodyne"+"/"
    copyfolder = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+split_list[5]+"/"+split_list[6]+"/"+split_list[7]+"/"+split_list[8]+"/"+"new_velodyne"+"/"
    # copyfolder = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+"data"+"/"+"kitti_1107"+"/"+split_list[7]+"/"+"velodyne"+"/"
    # print("folder",folder)
    # print(str(split_list))
    if not os.path.exists(copyfolder):
        os.makedirs(copyfolder)

    index = ""
    copy_file_name = ""
    copy_file_path = ""

    for split in split_list:
        if split.find("_2022") != -1:
            index = split
            # print(index)
        if split.find(".bin") != -1:
            copy_file_name = index + '_' + split
            # print(copy_file_name)
            copy_file_path = copyfolder+copy_file_name
            print(copy_file_path)

            # # print(copy_file_path)

            shutil.copy(file_path, copy_file_path)
