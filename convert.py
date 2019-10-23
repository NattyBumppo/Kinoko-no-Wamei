import csv

# Here's how to use this file. After generating full_mushrooms_jp_en.csv...
#
#     1) Run this script
#     2) Import the .csv file with UTF-8 encoding in Excel
#     3) Search-and-replace " ||| " with line break (CTRL-J)
#     4) Auto-fit all row heights with Home -> Row Height -> Autofit Row Height
#     5) Save as .xls and .xlsx files
#
# Why is this necessary? Because Excel is a hacked-together POS, basically.
# If you load the original .csv file in Excel with "open," it won't parse the
# encoding properly (Excel doesn't load UTF-8 by default for whatever damn reason).
# If you load the .csv file with the import tool, allowing you to switch the encoding,
# the line breaks won't be processed correctly. At any rate, the row heights are messed
# up and need to be changed manually as well.
#
with open('full_mushrooms_jp_en.csv', 'r', encoding='utf-8') as infile:
    with open('fixed.csv', 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=',', quotechar='"')

        for i, row in enumerate(reader):
            if i == 0:
                fieldnames = list(row.keys())
            
                writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()

            new_dict = {}
            for key in row.keys():
                value = row[key].replace('<br />', '').replace('\n', ' ||| ').replace('<i>', '').replace('</i>', '')

                new_dict[key] = value

            writer.writerow(new_dict)
