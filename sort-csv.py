import os
import csv
import pprint

if not os.path.exists('sorted-voies'):
    os.makedirs('sorted-voies')

if not os.path.exists('sorted-communes'):
    os.makedirs('sorted-communes')

def toSort(dpt):

    if dpt < 10:
        dpt = f'{int(dpt):02d}'

    str(dpt)

    with open(f'tosort/adresses-{dpt}.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)

        voies = []
        communes = []
        
        for i, row in enumerate(csvreader):
            voie = row[0].split(';')[4]
            commune = row[0].split(';')[7]
            post = row[0].split(';')[5]
            merged = [voie, commune]
            if not merged in voies:
                voies.append(merged)
            if not commune in communes:
                communes.append(commune)
            print('---')
            print('Voie: ' + voie)
            print('Commune: ' + commune)
            print('Post: ' + post)
        
        communes = sorted(communes)

    with open(f'sorted-voies/sorted-voies-list-{str(dpt)}.py', 'w', encoding='utf-8') as newSortedDptFile:
        newSortedDptFile.write(pprint.pformat(voies))
    with open(f'sorted-communes/sorted-communes-list-{str(dpt)}.py', 'w', encoding='utf-8') as newSortedCommunesFile:
        newSortedCommunesFile.write(pprint.pformat(communes))

for x in range(1, 96):
    if x == 20:
        continue
    toSort(x)