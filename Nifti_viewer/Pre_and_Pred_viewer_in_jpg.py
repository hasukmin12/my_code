
import os
import numpy as np
import cv2
from PIL import Image

try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')

img_nii = '/home/has/Datasets/_has_Task100_Bladder/case_00599/imaging.nii.gz'
seg_nii = '/home/has/Results/CT_2_inference_rst_120_e300_no_label2(reverse)/case_00012.nii.gz'


pre_out = '/home/has/Datasets/case_599_inference_rst/pre'
pred_out = '/home/has/Datasets/case_599_inference_rst/pred'



img = nib.load(img_nii).get_fdata()
seg = nib.load(seg_nii).get_fdata()

img = img.transpose(2,0,1)
seg = seg.transpose(2,0,1)

print(img.shape)
print(seg.shape)

z_axis = int(img.shape[0])
print(z_axis)
# cv2.imshow('pre',img[0])
# cv2.waitKey(0)

for i in range(z_axis):
    img_jpg = img[i]
    img_jpg = cv2.rotate(img_jpg,cv2.ROTATE_90_COUNTERCLOCKWISE)
    img_jpg = (img_jpg/256).astype('unit8')
    # img_jpg = cv2.cvtColor(img_jpg,cv2.COLOR_RGB2GRAY)
    print(img_jpg.max())
    # cv2.imwrite('/home/has/Datasets/case_599_inference_rst/pre/pre_{0:03}.jpg'.format(i),img_jpg)

pre_path = '/home/has/Datasets/case_599_inference_rst/pre'
pre_list = next(os.walk(pre_path))[2]
pre_list.sort()

# for list in pre_list:
#     out_path = os.path.join(pre_path,list)
#     img = cv2.imread(out_path, cv2.IMREAD_COLOR)
#     print(img.max())
#     cv2.imwrite('/home/has/Datasets/case_599_inference_rst/pred/pre_{0:03}.jpg'.format(pre_list.index(list)),img)





# # test_mask = test_mask.transpose(2,0,1)
# # print(test_mask.shape)
#
# z_axis = int(test_mask.shape[0])
#
# vol_numpy = np.zeros((z_axis,512,512))
#
# for i in range(z_axis):
#     # test_image[i] = cv2.rotate(test_image[i], cv2.ROTATE_90_COUNTERCLOCKWISE)
#     test_mask[i] = cv2.rotate(test_mask[i], cv2.ROTATE_90_CLOCKWISE)
#     vol_numpy[(z_axis-1) - i,:,:] = test_mask[i]






