import requests

for x in range(1, 95):
    if (x < 10):
        x = f'{int(x):02d}'
    # The department number 20 doesn't exist
    if x == 20:
        continue

    str(x)
    url = 'https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-' + x + '.csv.gz'
    r = requests.get(url, allow_redirects=True)

    with open(f'adresses-{x}.csv.gz', 'wb') as file:
        file.write(r.content)
