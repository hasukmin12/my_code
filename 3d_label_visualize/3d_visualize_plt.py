import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import nibabel as nib


# numpy.random.seed(29)

# img_path = '/home/has/Datasets/_has_Task120_Ureter/case_00000/segmentation.nii.gz'
img_path = '/home/has/Datasets/_has_Task113_Kid_with_Blad/case_00300/segmentation.nii.gz'
img = nib.load(img_path).get_fdata()
print(img.shape)

z,x,y = img.nonzero()
print(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, -z, zdir='z', c= 'red')
plt.savefig("demo2.png")

