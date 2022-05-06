import json

# with open('/home/has/Results/120_Ureter_test_summary.json','r') as my_json:
with open('/home/has/Results/125_Ureter_test_summary.json','r') as my_json:
    my_code = json.load(my_json)

print(my_code['results']['all'][0]['1']['Dice'])
# print(my_code['results']['all'][1]['1']['Dice'])

low = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0
cnt_7 = 0

# find min
print("dice score result")
for i in range(59):
    dice = my_code['results']['all'][i]['1']['Dice']
    if dice >= 0.7:
        cnt_7 +=1

    elif 0.7> dice >=0.6:
        cnt_6 += 1
    elif 0.6> dice >=0.5:
        cnt_5 += 1
    elif 0.5> dice>= 0.4:
        cnt_4 += 1
    elif 0.4> dice>= 0.3:
        cnt_3 += 1
        print(i+240)
    elif 0.3> dice:
        low += 1
        print(i)

print("dice 70>: " ,cnt_7)
print("dice 60>: ", cnt_6)
print("dice 50>: ", cnt_5)
print("dice 40>: ", cnt_4)
print("dice 30>: ", cnt_3)
print("dice >30: ", low)





# import matplotlib.pyplot as plt
#
# plt.plot(["low","0.3","0.4","0.5","0.6","0.7",],[low,cnt_3,cnt_4,cnt_5,cnt_6,cnt_7,])
# plt.ylabel('num of case')
# plt.xlabel('dice score')
# plt.show()