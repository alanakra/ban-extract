import os
import requests

if not os.path.exists('tosort'):
    os.makedirs('tosort')

for x in range(1, 96):
    # The department number 20 doesn't exist
    if x == 20:
        continue

    if x < 10:
        x = f'{int(x):02d}'
    else:
        x = str(x)

    str(x)
    url = 'https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-' + x + '.csv.gz'
    r = requests.get(url, allow_redirects=True)

    with open(f'tosort/adresses-{x}.csv.gz', 'wb') as file:
        file.write(r.content)
