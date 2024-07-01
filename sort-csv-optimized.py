import os
import pandas as pd
import pprint

if not os.path.exists('sorted-voies'):
    os.makedirs('sorted-voies')

if not os.path.exists('sorted-communes'):
    os.makedirs('sorted-communes')

def toSort(dpt):
    dpt = f'{int(dpt):02d}'

    file_path = f'tosort/adresses-{dpt}.csv'
    voies = set()
    communes = set()
    
    df = pd.read_csv(file_path, sep=';', usecols=[4, 5, 7], names=['voie', 'post', 'commune'], skiprows=1)

    for _, row in df.iterrows():
        voie = row['voie']
        commune = row['commune']
        post = str(row['post']).zfill(5)
        voies.add((voie, commune))
        communes.add(commune)
        print('---')
        print('Voie:', voie)
        print('Commune:', commune)
        print('Post:', post)

    voies = sorted(voies)
    communes = sorted(communes)

    with open(f'sorted-voies/sorted-voies-list-{dpt}.py', 'w', encoding='utf-8') as newSortedDptFile:
        newSortedDptFile.write(pprint.pformat(voies))
    with open(f'sorted-communes/sorted-communes-list-{dpt}.py', 'w', encoding='utf-8') as newSortedCommunesFile:
        newSortedCommunesFile.write(pprint.pformat(communes))

for x in range(1, 11):
    if x == 20:
        continue
    toSort(x)