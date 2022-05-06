import os
import numpy as np
import cv2
from PIL import Image
import shutil


try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')

# img_nii = '/home/has/Datasets/_has_Task100_Bladder/case_00599/imaging.nii.gz'
img_path = '/home/has/Datasets/의대 CT 추가 파일/CT/02691512박노섭190226/pre'
seg_nii = '/home/has/Results/CT_2_inference_rst_120_e300_no_label2(reverse)/case_00012.nii.gz'
img_list = next(os.walk(img_path))[2]
img_list.sort()

pre_out = '/home/has/Datasets/case_599_inference_rst/pre'
pre_list = next(os.walk(pre_out))[2]
pre_list.sort()
pred_out = '/home/has/Datasets/case_599_inference_rst/pred'

# for list in img_list:
#     input = os.path.join(img_jpg,list)
#     output = os.path.join(pre_out,'pre_{0:03d}.jpg'.format(img_list.index(list)))
#     shutil.copyfile(input,output)

seg = nib.load(seg_nii).get_fdata()
seg = seg.transpose(2,0,1)
print(seg.shape)
z_axis = int(seg.shape[0])
print(z_axis)

# cv2.imshow('pre',img[0])
# cv2.waitKey(0)

for i in range(z_axis):
    img_jpg = seg[i]
    img_jpg = cv2.rotate(img_jpg,cv2.ROTATE_90_COUNTERCLOCKWISE)
    # seg_3 = np.zeros((512,512,3))
    # for j in range(3):
    #     seg_3[:,:,j] = img_jpg
    # print(seg_3.shape)
    # print(seg_3.max())

    pre_path = os.path.join(pre_out,pre_list[i])
    print(pre_path)
    img = cv2.imread(pre_path, cv2.IMREAD_COLOR)
    print(img.max())



    # 이미지 겹치게 보이기
    add_img = img
    from skimage.util import montage

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img_jpg[x][y] != 0:
                add_img[x][y] = img_jpg[x][y]
                print(add_img[x][y])


    cv2.imwrite('/home/has/Datasets/case_599_inference_rst/pred/pred_{0:03}.jpg'.format(i),add_img)







