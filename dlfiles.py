import os
import requests
import gzip
import shutil

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
    url = f'https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-{x}.csv.gz'
    r = requests.get(url, allow_redirects=True)

    with open(f'tosort/adresses-{x}.csv.gz', 'wb') as file:
        file.write(r.content)

    gz_path = f'tosort/adresses-{x}.csv.gz'
    with open(gz_path, 'wb') as file:
        file.write(r.content)

    csv_path = f'tosort/adresses-{x}.csv'
    with gzip.open(gz_path, 'rb') as f_in:
        with open(csv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.remove(gz_path)