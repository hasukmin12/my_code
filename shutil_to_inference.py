import os
import shutil

path = "/home/has/Datasets/_has_Task126_Urinary"
path_list = next(os.walk(path))[1]
path_list.sort()
# print(path_list)

aim_path = '/home/has/Datasets/CT_2_inference7_150_240'
# aim_list = next(os.walk(aim_path))[1]
# aim_list.sort()
# print(aim_list[240:])

for case in path_list[150:]:
    input = os.path.join(path,case,'imaging.nii.gz')
    output = os.path.join(aim_path,'CT_{0:03d}_0000.nii.gz'.format(path_list.index(case)))

    shutil.copyfile(input,output)
    # print(input)
    # print(output)