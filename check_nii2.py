import os

import nibabel as nib

# 1. Proxy 불러오기


proxy = nib.load('/home/has/Datasets/BTCV_challenge_dataset/imageTr/DET0000201_avg.nii.gz')
# proxy = nib.load('/home/has/Datasets/211101_3D_AVIEW_CT/전체mask/abdomen_0007.nii.gz')


# proxy = nib.load('/home/has/Datasets/dcm_python/case_000/80920_portal_1mm.nii.gz')
# proxy = nib.load('/home/has/Datasets/CT_dcm2/case_001/case_01_Chest_Pre+_BYD-Abdomen_Thorax_20180528105732_14.nii.gz')
# proxy = nib.load('/home/has/Datasets/CT_to_inference/CT_000_0000.nii.gz')
# proxy = nib.load('/home/has/Datasets/kits19/data/case_00000/imaging.nii.gz') #(611, 512, 512)
# proxy = nib.load('/home/has/Results/output2/CT_000.nii.gz')

# 2. Header 불러오기
header = proxy.header

# 3. 원하는 Header 불러오기 (내용이 문자열일 경우 숫자로 표현됨)
header_size = header['sizeof_hdr']

# 2. 전체 Image Array 불러오기
arr = proxy.get_fdata()

# 3. 원하는 Image Array 영역만 불러오기
sub_arr = proxy.dataobj[..., 0:5]


# print(arr.shape)
# arr = arr.transpose((1,2,0))

print(arr.shape)
print(arr.max())
print(arr.min())
# print(arr)