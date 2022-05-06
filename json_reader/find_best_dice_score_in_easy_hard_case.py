import json

with open('/home/has/Results/295_Ureter_test_summary_CADD.json','r') as my_json:
    my_code = json.load(my_json)

min = 1

easy_list = [0,1,2,3,4,6,7,8,10,11,12,13,14,15,17,23,24,25,26,27,29,31,33,34,36,37,38,39,41,43,44,45,46,47,49,51,52,53,54,55,56,57,58,61,62,63,64,65,66,67,68]
hard_list = [5,9,16,18,19,20,21,22,28,30,32,35,42,48,50,59,60]

easy_score = []
hard_score = []

print(len(easy_list))
print(len(hard_list))
print()
print("easy_list")
# hard_list
# find min
print("who is min")
for i in easy_list:# 60):
    dice = my_code['results']['all'][i]['1']['Dice']
    easy_score.append(dice)
    if dice <= min:
        min = dice
        print(i+301)
        print(min)

print("")
print("now we start")
print("who is max")
max = 0
for i in easy_list:
    dice = my_code['results']['all'][i]['1']['Dice']
    if dice >= max:
        max = dice
        print(i+301)
        print(max)


print()
print()
print("hard_list")
# find min
print("who is min")
for i in hard_list:# 60):
    dice = my_code['results']['all'][i]['1']['Dice']
    hard_score.append(dice)
    if dice <= min:
        min = dice
        print(i+301)
        print(min)


# find max
print("")
print("now we start")
print("who is max")
max = 0
for i in hard_list:
    dice = my_code['results']['all'][i]['1']['Dice']
    if dice >= max:
        max = dice
        print(i+301)
        print(max)

print()
easy_score.sort()
hard_score.sort()
print(easy_score)
print(hard_score)
print(len(easy_score))
print(len(hard_score))


result = 0
for val in easy_score:
    result += val # 하나하나 더하기 # 평균 구하기 print(f"average : {result / len(arr)}")
print("easy_score_average : ",result/len(easy_score))

result = 0
for val in hard_score:
    result += val
print("hard_score_average : ",result/len(hard_score))

total_score = easy_score + hard_score
result = 0
for val in total_score:
    result += val
print("total_score_average : ", result/len(total_score))





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