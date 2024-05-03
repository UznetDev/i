N=5
M=3
data = {'Sanjar': [1, 5],
        'Baxrom': [3, 5],
        'Kamola': [1, 2]}

bekat = {f'{i}-{i+1}':0 for i in range(1, N)}
for i in data.values():
    for x in range(i[0], i[1]):
        bekat[f'{x}-{x+1}'] += 1

max_v = bekat[max(bekat, key=lambda x: bekat[x])]
for i in bekat:
     if bekat[i] == max_v:
             print(i)



