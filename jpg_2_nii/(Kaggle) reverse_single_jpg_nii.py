
import skimage, os
from skimage.morphology import ball, disk, dilation, binary_erosion, remove_small_objects, erosion, closing, reconstruction, binary_closing
from skimage.measure import label,regionprops, perimeter
from skimage.morphology import binary_dilation, binary_opening
from skimage.filters import roberts, sobel
from skimage import measure, feature
from skimage.segmentation import clear_border
from skimage import data
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.misc
import numpy as np

import cv2



all_masks = '/home/has/Datasets/Ureter_239/ureter_seg_239.nii.gz'

try:
    import nibabel as nib
except:
    raise ImportError('Install NIBABEL')

test_mask=nib.load(all_masks).get_fdata()

# test_mask = test_mask.transpose(2,0,1)
# print(test_mask.shape)

z_axis = int(test_mask.shape[0])

vol_numpy = np.zeros((z_axis,512,512))

for i in range(z_axis):
    # test_image[i] = cv2.rotate(test_image[i], cv2.ROTATE_90_COUNTERCLOCKWISE)
    test_mask[i] = cv2.rotate(test_mask[i], cv2.ROTATE_90_CLOCKWISE)
    vol_numpy[(z_axis-1) - i,:,:] = test_mask[i]



# test_mask2 = vol_numpy.transpose(1,2,0)
# print(test_mask2.shape)

xform = np.eye(4) * 2
label_Nifti = nib.nifti1.Nifti1Image(vol_numpy, xform)

output_path = '/home/has/Datasets/Ureter_239/ureter_seg_239.nii.gz'

nib.save(label_Nifti, output_path)
print("save nii")



