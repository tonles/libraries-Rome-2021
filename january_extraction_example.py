"""""
Extracting the data for january 2021
"""""

import pandas as pd
import numpy as np
import re

# Loading datasets
jan = pd.read_json('det_p_meseprec_02.json')
jan_df = jan['tabella'].apply(pd.Series)

# Extracting only "book" category
group_rule = jan_df.groupby(jan_df['Cod. tipo documento'])
books = group_rule.get_group('LM').reset_index()

# Extracting author
author = []
for i in range(len(books['Titolo'])):
    author_a = books['Titolo'][i].split(' / ')
    try:
        author_b = author_a[1].split(' ; ')
        author_c = author_b[0].split('. ')
        author.append(author_c[0])
    except (IndexError, AttributeError):
        author.append(np.nan)

# Extracting n° of pages
pages_regex = re.compile("(?<=; )\d\d(\d)?(\d)?(?= p)|(?<=- )\d\d(\d)?(\d)?|(?<=, )\d\d(\d)?(\d)?(?= p)|"
                         "(?<=. )\d\d(\d)?(\d)?(?= p)|(?<=- \[)\d\d(\d)?(\d)?(?=\])")
pages = []
for i in range(len(books['Titolo'])):
    try:
        if pages_regex is not None:
            test_page = pages_regex.search(books['Titolo'][i]).group(0)
            pages.append(test_page)
        else:
            pages.append(np.nan)
    except AttributeError:
        pages.append(np.nan)

# Extracting publishing house
ph = []
for i in range(len(books['Titolo'])):
    ph_a = books['Titolo'][i].split(' / ')
    try:
        ph_b = ph_a[1].split(' : ')
        ph_c = ph_b[1].split(', ')
        ph.append(ph_c[0])
    except IndexError:
        ph.append(np.nan)

# Create a DataFrame for each of the 3 features extracted
df_author = pd.DataFrame(author, columns=['Author'])
df_pages = pd.DataFrame(pages, columns=['Number of pages'])
df_ph = pd.DataFrame(ph, columns=['Publishing House'])

# Merge the above DataFrame in a single one and export as csv file
january_extraction = pd.concat([df_author, df_pages, df_ph], axis=1)
january_extraction.to_csv(r'C:\YOURPATH\01_january_extraction'r'.csv',
                          index=False)

books.to_csv(r'C:\YOURPATH\01_january_books'r'.csv', index=False)
