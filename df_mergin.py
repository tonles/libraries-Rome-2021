import pandas as pd

# Loading datasets
jan = pd.read_csv('01_january_extraction.csv')
feb = pd.read_csv('02_february_extraction.csv')
mar = pd.read_csv('03_march_extraction.csv')
apr = pd.read_csv('04_april_extraction.csv')
may = pd.read_csv('05_may_extraction.csv')
jun = pd.read_csv('06_june_extraction.csv')
jul = pd.read_csv('07_july_extraction.csv')
aug = pd.read_csv('08_august_extraction.csv')
sep = pd.read_csv('09_september_extraction.csv')
octo = pd.read_csv('10_october_extraction.csv')
nov = pd.read_csv('11_november_extraction.csv')
dec = pd.read_csv('12_december_extraction.csv')

books_jan = pd.read_csv('01_january_books.csv', low_memory=False)
books_feb = pd.read_csv('02_february_books.csv', low_memory=False)
books_mar = pd.read_csv('03_march_books.csv', low_memory=False)
books_apr = pd.read_csv('04_april_books.csv', low_memory=False)
books_may = pd.read_csv('05_may_books.csv', low_memory=False)
books_jun = pd.read_csv('06_june_books.csv', low_memory=False)
books_jul = pd.read_csv('07_july_books.csv', low_memory=False)
books_aug = pd.read_csv('08_august_books.csv', low_memory=False)
books_sep = pd.read_csv('09_september_books.csv', low_memory=False)
books_oct = pd.read_csv('10_october_books.csv', low_memory=False)
books_nov = pd.read_csv('11_november_books.csv', low_memory=False)
books_dec = pd.read_csv('12_december_books.csv', low_memory=False)

# Merging single months into one single DataFrame (year)
year_2021_title = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec])
year_2021_books = pd.concat([books_jan, books_feb, books_mar, books_apr, books_may, books_jun, books_jul, books_aug,
                             books_sep, books_oct, books_nov, books_dec])

# Create a support variable
support_2021 = year_2021_books[['Genere 1', 'Anno di pubblicazione', 'Lingua 1', 'Biblioteca movimento',
                              'Tipo utente movimento', 'Eta\' utente-movimento', 'Data inizio movimento',
                              'Data stima fine movimento', 'Data fine movimento', 'Tipo movimento']]

books_2021 = pd.concat([year_2021_title, support_2021], axis=1)

column_names = ['Autore', 'Numero_pagine', 'Casa_editrice', 'Genere_1', 'Anno_pubblicazione', 'Lingua_1',
              'Biblioteca_movimento', 'Tipo_utente_movimento', "Eta'_utente_movimento", 'Data_inizio_movimento',
              'Data_stima_fine_movimento', 'Data_fine_movimento', 'Tipo_movimento']

books_2021.columns = column_names

books_2021.to_csv(r'C:\YOURPATH\books_2021'r'.csv',
                          index=False)
