import numpy as np
import os
import nibabel as nib
import shutil


path = '/home/has/Datasets/_has_Task273_Urinary'
path_list = next(os.walk(path))[1]
path_list.sort()
print(path_list)
print()

list_u = []
list_b = []
list_k = []

u = 0
b = 0
k = 0
total = 0
for case in path_list[:299]:
    print()
    print(case)
    case_path = os.path.join(path, case, 'segmentation.nii.gz')
    seg = nib.load(case_path).get_fdata()
    z_axis = int(seg.shape[0])

    for z in range(0, z_axis):
        for x in range(0, 512):
            for y in range(0, 512):
                if seg[z][x][y] == 1:
                    u += 1
                elif seg[z][x][y] == 2:
                    b += 1
                elif seg[z][x][y] == 3:
                    k += 1

    total = u + b + k
    print(u/total)
    print(b/total)
    print(k/total)
    print((total / u) / (total / u + total / b + total / k))
    print((total / b) / (total / u + total / b + total / k))
    print((total / k) / (total / u + total / b + total / k))

print()
print(u/total)
print(b/total)
print(k/total)

print()
print(total/u)
print(total/b)
print(total/k)

print()
print((total/u) / (total/u + total/b + total/k))
print((total / b) / (total / u + total / b + total / k))
print((total / k) / (total / u + total / b + total / k))









