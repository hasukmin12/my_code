import json

import numpy as np

with open('/home/has/Results/275_Ureter_test_summary_Res.json','r') as my_json:
    my_code = json.load(my_json)


easy_list = [0,1,2,3,4,6,7,8,10,11,12,13,14,15,17,23,24,25,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,49,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68]
hard_list = [5,9,16,18,19,20,21,22,28,30,32,35,42,48,50,59,60]

easy_score = []
hard_score = []

pred_score_easy = []
recal_score_easy = []
jac_score_easy = []

pred_score_hard = []
recal_score_hard = []
jac_score_hard = []

for i in easy_list:# 60):
    dice = my_code['results']['all'][i]['1']['Dice']
    easy_score.append(dice)
    pred = my_code['results']['all'][i]['1']['Precision']
    pred_score_easy.append(pred)
    jac = my_code['results']['all'][i]['1']['Jaccard']
    jac_score_easy.append(jac)
    rec = my_code['results']['all'][i]['1']['Recall']
    recal_score_easy.append(rec)


for i in hard_list:# 60):
    dice = my_code['results']['all'][i]['1']['Dice']
    hard_score.append(dice)
    pred = my_code['results']['all'][i]['1']['Precision']
    pred_score_hard.append(pred)
    jac = my_code['results']['all'][i]['1']['Jaccard']
    jac_score_hard.append(jac)
    rec = my_code['results']['all'][i]['1']['Recall']
    recal_score_hard.append(rec)



easy_score.sort()
hard_score.sort()


total_score = easy_score + hard_score
pred_score = pred_score_easy + pred_score_hard
recal_score = recal_score_easy + recal_score_hard
jac_score = jac_score_easy + jac_score_hard

result = 0
for val in total_score:
    result += val



print("total_dice_score_average : ", np.average(total_score))
print("total_precision_average : ", np.average(pred_score))
print("total_recal_average : ", np.average(recal_score))
print("total_jac_average : ", np.average(jac_score))
print()
print("easy_dice_score_average : ", np.average(easy_score))
print("easy_precision_average : ", np.average(pred_score_easy))
print("easy_recal_average : ", np.average(recal_score_easy))
print("easy_jac_average : ", np.average(jac_score_easy))
print()
print("hard_dice_score_average : ", np.average(hard_score))
print("hard_precision_average : ", np.average(pred_score_hard))
print("hard_recal_average : ", np.average(recal_score_hard))
print("hard_jac_average : ", np.average(jac_score_hard))
# result = 0
# for val in pred_score:
#     result += val
# print("total_precision_average : ", result/len(pred_score))
#
# for val in recal_score:
#     result += val
# print("total_recal_average : ", result/len(pred_score))
#
# result = 0
# for val in jac_score:
#     result += val
# print("total_jac_average : ", result/len(pred_score))








# # draw plot
# import matplotlib.pyplot as plt
# plt.figure()
#
# # print(int)
# # print(int/22)
# # weight.sort()
# # print(weight)
# # # t.hist(weight, label='bins=10')
#
# plt.hist(easy_score, bins=50,  color='orange', range=(0,1))
# plt.ylim(0,6)
# plt.xlabel("Dice score",fontsize=12)
# plt.ylabel("Count",fontsize=12)
# plt.legend()
# plt.show()
#
# plt.hist(hard_score, bins=50,  color='green', range=(0,1))
# plt.ylim(0,6)
# plt.xlabel("Dice score",fontsize=12)
# plt.ylabel("Count",fontsize=12)
# plt.legend()
# plt.show()