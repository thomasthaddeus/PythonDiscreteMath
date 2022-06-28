cities = {
    'Montreal': 584,
    'Chicago': 438,
    'London': 982,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)
