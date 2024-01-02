from copy import deepcopy

players = [
    {
        'first_name': 'John',
        "last_name": 'Doe',
        'rank': 3,
    }, {
        'first_name': 'Kevin',
        "last_name": 'McDonald',
        'rank': 1,
    },
    {
        'first_name':'Brad',
        "last_name":'Kelvin',
        'rank':2,
    },
]

# print(sorted(players, key=lambda player: player['rank'], reverse=True))


def check_top_3_player(player):
    updated = deepcopy(player)
    updated['is_top_3'] = True if updated['rank'] <= 3 else False
    return updated

top = map(check_top_3_player, players)

# print(list(top))

all_mc = filter(lambda player: True if player['last_name'] == "McDonald" else False, players)
# print(list(all_mc))

names = ['Ion', 'Elena', 'Maria','George']
cities = ['Cluj-Napoca', 'Bucuresti', 'Iasi', 'Timisoara']
jobs = ['developer', 'qa', 'designer', 'hr']

all=[]
for zip_item in zip(names, cities, jobs):
    name, city, job = zip_item
    all.append({
        'name':name,
        'city':city,
        'job':job
    })


# print(all)

list  = [1,2,3,4,5]
squared=[ i**2 for i in list]
print(squared)