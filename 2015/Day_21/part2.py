from itertools import combinations

content = open("input.txt","r").read()
stats = content.split("\n")

boss = {}
player = {}

player['HP'] = 100

for stat in stats:
    stat = stat.split()
    if len(stat) == 3:
        boss['HP'] = int(stat[2])
    else:
        boss[stat[0].strip(':')] = int(stat[1])

wepons = {'Dagger':[8,4,0],'Shortsword':[10,5,0],'Warhammer':[25,6,0],'Longsword':[40,7,0],'Greataxe':[74,8,0]}
armors = {'Leather':[13,0,1],'Chainmail':[31,0,2],'Splintmail':[53,0,3],'Bandedmail':[75,0,4],'Platemail':[102,0,5]}
rings = {'1':[25,1,0],'2':[50,2,0],'3':[100,3,0],'4':[20,0,1],'5':[40,0,2],'6':[80,0,3]}

def player_vs_boss(player,boss):
    turn = 0
    p_HP = player['HP']
    b_HP = boss['HP']
    while p_HP > 0 and b_HP > 0:
        if turn==0:
            b_HP -= max(1,player['Damage'] - boss['Armor'])
            turn = 1 - turn
        else:
            p_HP -= max(1,boss['Damage'] - player['Armor'])
            turn = 1 - turn

    if p_HP > 0:
        return False
    else:
        return True

total_cost = 0

for wepon in wepons:
    player['Damage'] = wepons[wepon][1]
    player['Armor'] = 0
    cost = wepons[wepon][0]
    if player_vs_boss(player, boss):
        total_cost = max(total_cost, cost)
    for armor in armors:

        # With No ring
        player['Damage'] = wepons[wepon][1] + armors[armor][1]
        player['Armor'] = wepons[wepon][2] + armors[armor][2]
        cost = wepons[wepon][0] + armors[armor][0]
        if player_vs_boss(player, boss):
            total_cost = max(total_cost, cost)

        # With 1 Ring
        for ring in rings:
            player['Damage'] = wepons[wepon][1] + armors[armor][1] + rings[ring][1]
            player['Armor'] = wepons[wepon][2] + armors[armor][2] + rings[ring][2]
            cost = wepons[wepon][0] + armors[armor][0] + rings[ring][0]
            if player_vs_boss(player, boss):
                total_cost = max(total_cost, cost)

        # With 2 rings
        for combo in combinations(rings, 2):
            player['Damage'] = wepons[wepon][1] + armors[armor][1] + rings[combo[0]][1] + rings[combo[1]][1]
            player['Armor'] = wepons[wepon][2] + armors[armor][2] + rings[combo[0]][2] + rings[combo[1]][2]
            cost = wepons[wepon][0] + armors[armor][0] + rings[combo[0]][0] + rings[combo[1]][0]
            if player_vs_boss(player, boss):
                total_cost = max(total_cost, cost)

print(total_cost)