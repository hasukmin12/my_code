import json

with open('/home/has/Results/124_Urinary_train_summary.json','r') as my_json:
    my_code = json.load(my_json)

print(my_code['results']['all'][0]['3']['Dice'])
print(my_code['results']['all'][1]['3']['Dice'])


sum_of_dice = 0
for i in range(150):
    dice = my_code['results']['all'][i]['3']['Dice']
    print(dice)
    sum_of_dice = sum_of_dice + dice
    print(sum_of_dice)

print(sum_of_dice)
print(sum_of_dice/151)


