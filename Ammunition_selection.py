from collections import defaultdict

def greedy(weight_per_pack, damage_per_pack,total_weight):
     #making an array for storing damage to weight ratio
    damage_capacity_by_weight = [(damage/weight,i) for (i,weight,damage) in zip(range(len(damage_per_pack)),weight_per_pack, damage_per_pack)]
     #sorting them in decreasing order
    damage_capacity_by_weight = sorted(damage_capacity_by_weight,reverse = True)
    #dictionary for storing the ratios in which ammunition should be taken
    ratio = defaultdict(lambda: 0)
    #stores current ammunition's weight
    weight_picked = 0
    for (damage_weight_ratio,i) in damage_capacity_by_weight:
        if(total_weight <= weight_picked):#stopping if weght restriction reached
            break
        #else picking the ammunition with higher damage to weight ratio
        ratio[i] = min(weight_per_pack[i],total_weight-weight_picked)/total_weight
        weight_picked += min(weight_per_pack[i],total_weight-weight_picked)

        print("Ammunition =>Ratio \n--------------------------------------" )
        for i in range(len(damage_per_pack)):
             print(" ",(i+1)," => ",(ratio[i]))#testing
        

weight_per_pack = [10,30,18,80,10,20]
damage_per_pack = [20,40,38,60,15,22]
greedy(weight_per_pack, damage_per_pack,118)