import shutil
import os


path = '/home/has/Datasets/_has_Task123_Ureter'
aim_path = '/home/has/Datasets/CT_2_inference5_test_all'

path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list[210:300])

for case in path_list[210:300]:
    input_path = os.path.join(path,case,'imaging.nii.gz')
    output_path = os.path.join(aim_path,"CT_{0:03d}_0000.nii.gz".format(path_list.index(case)))
    shutil.copyfile(input_path,output_path)
