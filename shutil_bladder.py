import os
import shutil

path = "/home/has/Datasets/Bladder_240.nii(turn)"
path_list = next(os.walk(path))[2]
path_list.sort()
# print(path_list)

aim_path = '/home/has/Datasets/_has_Task102_Bladder_reverse'
aim_list = next(os.walk(aim_path))[1]
aim_list.sort()
# print(aim_list[240:])

for case in path_list:
    input = os.path.join(path,case)
    output = os.path.join(aim_path,aim_list[path_list.index(case)+240],'segmentation.nii.gz')

    shutil.copyfile(input,output)
    # print(input)
    # print(output)