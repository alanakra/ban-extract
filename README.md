# MATRIMOINE PROJECT - EXTRACTING DATA FROM THE NATIONAL ADDRESS DATABASE (BASE ADRESSE NATIONALE)

This repo contains scripts for downloading addresses in France via the National Address Base (Base Adresse Nationale).

The `dlfiles.py` script makes it easier to download ZIP files. By default, the loop goes from 1 (Département de l'Ain) to 95 (Département du Val d'Oise). For overseas departments, simply change the parameters of the `range()` function.

Once the files have been unzipped, unpack them in a folder called `tosort`.

[!WARNING]
Check that files do not contain commas `,`. If not, remove them with CTRL+F and replace with a blank character. Data is separated by semicolons `;`.

When all the files have been executed, you can now run either the `sort-csv-optimized.py` script or the `sort-csv-optimized.py` script, which is much faster to run. The outputs will appears in `sorted-communs` and `sorted-voies` directories.