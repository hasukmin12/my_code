import os
import shutil

blad_path = '/home/has/Datasets/second'
case_list = next(os.walk(blad_path))[1]
case_list.sort()
print(case_list)

seg_path = '/home/has/Datasets/(reserve)bladder_seg_nii_2'
blad_list = next(os.walk(seg_path))[2]
blad_list.sort()
print(blad_list)

for case in case_list:
    number = int(case_list.index(case))
    print(number+300)
    # if number ==240:
    #     break
    shutil.copyfile(os.path.join(seg_path,blad_list[number]), os.path.join(blad_path, case, 'segmentation.nii.gz'))
