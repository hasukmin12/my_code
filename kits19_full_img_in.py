import os
import shutil

path = '/home/has/Datasets/_has_Task105_Blad_Kid'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)


path_kid_img = '/home/has/Datasets/kits19/data'
case_list = next(os.walk(path_kid_img))[1]
case_list.sort()
print(case_list)

for case in case_list:
    print(case)
    input = os.path.join(path_kid_img,case,'imaging.nii.gz')
    output = os.path.join(path,case,'imaging.nii.gz')

    shutil.copyfile(input,output)
    
    