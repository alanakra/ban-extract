# MATRIMOINE PROJECT - EXTRACTING DATA FROM THE NATIONAL ADDRESS DATABASE (BASE ADRESSE NATIONALE)

This repo contains scripts for downloading addresses in France via the National Address Base (Base Adresse Nationale).

Install all dependencies with: `pip install -r requirements.txt`.

The `dlfiles.py` script makes it easier to download ZIP files. By default, the loop goes from 1 (Département de l'Ain) to 95 (Département du Val d'Oise). For overseas departments, simply change the parameters of the `range()` function.

[!WARNING]
Check that files do not contain commas `,`. If not, remove them with CTRL+F and replace with a blank character. Data is separated by semicolons `;`.

When all the files have been executed, you can now run `sort-csv.py`. The outputs will appears in `sorted-communes` and `sorted-voies` directories.