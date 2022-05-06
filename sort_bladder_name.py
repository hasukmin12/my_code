import os
import shutil

path = '/home/has/Datasets/CT_bladder_labeling_Mask7_2'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)

for case in path_list:
    path_in = os.path.join(path,case)
    path_out = '/home/has/Datasets/CT_bladder_labeling_Mask7_2_2'
    name = 'case_{0:05d}'.format(int(path_list.index(case)) + 300)
    if os.path.isdir(path_out)==False:
        os.makedirs(path_out)
    shutil.copytree(path_in,os.path.join(path_out,name))
