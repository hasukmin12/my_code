import matplotlib.pyplot as plt
import  json
weight = []

with open('/home/has/Results/192_Ureter_test_t22_e450_summary.json','r') as my_json:
    my_code = json.load(my_json)

int = 0
for i in range(22):
    dice = my_code['results']['all'][i]['1']['Dice']
    weight.append(dice)
    if dice > 0.65:
        int +=1

print(int)
print(int/22)
weight.sort()
print(weight)
# t.hist(weight, label='bins=10')
plt.hist(weight, bins=73,  color='orange', range=(0,1))
plt.ylim(0,6)
plt.xlabel("Dice score",fontsize=12)
plt.ylabel("Count",fontsize=12)
plt.legend()
plt.show()
