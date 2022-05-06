import json

with open('/home/has/Results/124_Urinary_test_summary_blad_add.json','r') as my_json:
    data_124 = json.load(my_json)

with open('/home/has/Results/120_Ureter_test_summary.json','r') as my_json:
    data_120 = json.load(my_json)



# print(data_124['results']['all'][0]['1']['Dice'])


cnt = 0


for i in range(89):
    dice_124 = data_124['results']['all'][i]['1']['Dice']
    dice_120 = data_120['results']['all'][i]['1']['Dice']


    if dice_124 < dice_120:
        print(i+210)
        print(dice_120)
        print(dice_124)
        print("")
        cnt += 1

print(cnt)



