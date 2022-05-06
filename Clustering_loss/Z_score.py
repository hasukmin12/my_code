import os
import numpy as np
import nibabel as nib
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing
from Clustering_loss.Z_score_for_blob_detection import blob_detecter
import cv2


# path = '/home/has/Datasets/_has_Task123_Ureter/case_00000/segmentation.nii.gz'
path = '/home/has/Results/inf_2_GT_130/case_00251.nii.gz'
mask = nib.load(path).get_fdata()

z_axis = int(mask.shape[0])

pi_list = [[0,0],[0,0]] * z_axis
vi = [0,0]

esti_pi = [0,0]
error_list = []
left_err = []
right_err = []


# print(pi_list[2])

cnt = 0
error = 0
first = 0



for z in range(0, z_axis):
    if mask[z].max() == 1:
        # if mask[z + 1].max() == 0:
        #     continue

        # cnt += 1
        blob = blob_detecter(mask[z])
        if blob[0].max() != 0 and blob[1].max() != 0:
            first += 1
            cnt += 1 # 양쪽에서 blob이 1개만 찍히는경우가 있어서 그 경우엔 cnt에 포함 안시키도록 구현함
            # print("two blob is exist")
            # print(z)
            # print(blob_detecter(mask[z]))
            # print("")
            if blob[2].max() != 0:
                error += 1
                print("there is three points")
                continue
                # print(z)
                # print("")


            # 여기서부터 아이디어 제안

            pi_list[z][0], pi_list[z][1] = blob[0], blob[1]

            if first == 2:
                vi[0] = pi_list[z-1][0] - pi_list[z][0]
                vi[1] = pi_list[z-1][1] - pi_list[z][1]

                # print(vi[0], vi[1])
                # print(pi_list[z][0], pi_list[z-1][0])

                esti_pi = np.array([pi_list[z][0] + vi[0], pi_list[z][1] + vi[1]])
                print("first cnt")
                print(z)
                print(vi[0], vi[1])
                print(esti_pi)
                print("")



            if first > 2:
                vi[0] = pi_list[z - 1][0] - pi_list[z][0]
                vi[1] = pi_list[z - 1][1] - pi_list[z][1]

                # 여기서 estimation과 prediction의 차이를 계산

                print(z)
                print(cnt)
                print(esti_pi[0])
                print(pi_list[z][0])
                print("")

                left_err = esti_pi[0] - pi_list[z][0]
                right_err = esti_pi[1] - pi_list[z][1]

                err = [left_err, right_err]
                error_list.append(err)


                esti_pi = np.array([pi_list[z][0] + vi[0], pi_list[z][1] + vi[1]])


        else:
            # print("z axis : ", z)
            # print(blob[0].max())
            # print(blob[1].max())
            # print("there is no blob")
            # print("")
            cnt += 1
            error += 1



print(error_list)
precessed_data = error_list.copy()


print(precessed_data[0][0][0])
print(precessed_data[0])
print(len(precessed_data))

array_list = []
for i in range(18):
    for j in range(2):
        array_list.append(precessed_data[i][j])

print(array_list)
print(len(array_list))

x = []
y = []
for k in range(36):
    x.append(array_list[k][0])
    y.append(array_list[k][1])

print(x)
print(y)


plt.scatter(x, y)
plt.show()






# # 데이터 전처리
# scalar = preprocessing.MinMaxScaler()
# precessed_data[['x','y']] = scalar.fit_transform(preprocessed[['x','y']])
#
#
# plt.figure(figsize = (10,6))
# estimator = KMeans(n_cluster = 2)
# ids = estimator.fit_predict(precessed_data[['x','y']])
#
# plt.scatter(precessed_data['x'],precessed_data['y'], c=ids)
# plt.show()















if error == 0:
    z_score = 0
else:
    z_score = error / cnt

print("cnt : ", cnt)
print("error : ", error)
print("z_score : ", z_score)