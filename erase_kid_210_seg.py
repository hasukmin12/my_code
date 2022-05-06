import os
import numpy as np
import shutil

path = '/home/has/Datasets/_has_Task105_Blad_Kid'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list[210:300])

for case in path_list[540:600]:
    seg_path = os.path.join(path,case,'segmentation.nii.gz')
    if os.path.isfile(seg_path)==True:
        print(case)
        # os.remove(seg_path)