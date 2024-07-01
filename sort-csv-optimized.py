import os
import pandas as pd
import pprint

if not os.path.exists('sorted-voies-cut'):
    os.makedirs('sorted-voies-cut')

if not os.path.exists('sorted-communes-cut'):
    os.makedirs('sorted-communes-cut')

def toSort(dpt):
    dpt = f'{int(dpt):02d}'

    file_path = f'tosort/adresses-{dpt}.csv'
    voies = set()
    communes = set()
    
    df = pd.read_csv(file_path, sep=';', usecols=[4, 5, 7], names=['voie', 'post', 'commune'], skiprows=1)

    prefix = {"Boule lyonnaise ", "Boulodrome ", "Boulodrome couvert ", "Centre nautique ", "Centre Sportif ", "City Stade ", "Complexe ", "Complexe sportif ", "Dojo ", "École De Danse ", "Espace ", "Halle ", "Halle des sports ", "Halle sportive ", "Gymnase ", "Gymnase scolaire ", "Jeu de boules ", "Le centre ", "Mini Football ", "Palais des Sports ", "Piscine ", "Piscine municipale ", "Piste d'athlétisme ", "Piste d'athletisme ", "Plateau Sportif ", "Plateaux sportifs ", "Salle ", "Salle de boxe ", "Salle de sport ", "Salle de sports ", "Salle omnisports ", "Skate-Park ", "Square ", "Stade ", "Stade municipal ", "Tennis Club ", "Tennis Club municipal ", "Terrain ", "Terrain de football ", "Terrain de proximité ", "Vélodrome ", ".*Vélodrome ","Crèche( Municipale| PMI| public| privé)* ", "Collège( | public| privé)* ", "École ([ÉE]l[eé]mentaire|maternelle|primaire|technique|technologique)*( |Centre |d'application )*(privée|publique)*[ ]*", "Espace ", "Groupe scolaire ", "Institut ", "Institution ", "Lycée( | général| général et technologique| polyvalent| professionnel| professionnel| technologique| [Tt]echnique)*( | et technologique)*( | public| privé|.*restauration)* ", "PMI ","Biblioth[èe]que( | centrale| communale| départementale| municipale| universitaire)* ", "M[ée]diath[èe]que( | centrale| communale| départementale| municipale)* ","All[ée]e ", "Avenue ", "Boulevard ", "Chemin ", "Cours ", "Galerie ", "Impasse ", "Jardin ", "Mail " , "Passage " , "Place ", "Quai ", "R[ée]sidence ", "Rue ","Ruelle ", "Sente ", "Sentier ", "Square ", "Villa "}

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

    with open(f'sorted-voies-cut/sorted-voies-cut-list-{dpt}.py', 'w', encoding='utf-8') as newSortedDptFile:
        newSortedDptFile.write(pprint.pformat(voies))
    with open(f'sorted-communes-cut/sorted-communes-cut-list-{dpt}.py', 'w', encoding='utf-8') as newSortedCommunesFile:
        newSortedCommunesFile.write(pprint.pformat(communes))

# for x in range(1, 11):
#     if x == 20:
#         continue
toSort(34)