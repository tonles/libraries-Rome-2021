# Analysis of the transactions of Roman public libraries in 2021
Given my passion for reading, in order not to separate myself too much from books, I decided to analyze the transactions carried out
throughout 2021 between all public libraries in Rome, in order to identify trends and potentially optimize processes.

The source of the data is the [_Open Data_](https://dati.comune.roma.it/catalog/dataset/d146) site of the city of Rome.

Note: the attributes are written in the original language (Italian).

## Getting the data & understanding the dataset
From the above-mentioned site, I downloaded the data for every month in _json_ format. Since every month is referred to the transactions occured in the previous month, in order to get the data for all of 2021 I downloaded the files ranging from February 2021 to January 2022.

In addition to the actual data I downloaded a file containing the metadata, so that I can start to get a feel for the dataset.

Starting from the initial 23 attributes, for the purpose of my analysis I've decided to select the following 11 features:
1) Titolo (title, with other ISBD fields)
2) Genere_1 (main genre)
3) Anno_pubblicazione (year of publication)
4) Lingua_1 (main language)
5) Biblioteca_movimento (library)
6) Tipo_utente_movimento (user type)
7) Eta'_utente_movimento (user age)
8) Data_inizio_movimento (transaction start date)
9) Data_stima_fine_movimento (transaction estimate end date)
10) Data_fine_movimento (transaction end date)
11) Tipo_movimento (transaction type)

## Cleaning the data
Since the feature _Titolo_ contains in the same value different elements carried by the ISBD ([International Standard Bibliographic Description](https://en.wikipedia.org/wiki/International_Standard_Bibliographic_Description)), e.g.: 

![](/images/ISBD.png)

I had to perform some cleaning operations to extract the necessary information and put them each on a different column. 

I first worked on the single month, in order to verify the effectiveness of the cleaning operations, then I extended it to the other months.

The information to be extracted from _Titolo_ are: author, publishing house and number of pages. For the first two, I solved using the _.split()_ method,
whereas for the number of pages I had to go step by step building different regular expressions, in order to improve their efficiency.

Since the records have not all been filled in the same way, the extraction of the number of pages does not work equally for all the records; 
as a result there is a failure to extract the number of pages from _Titolo_, therefore null values are obtained.

With the regular expression _pages_regex_ (please refer to lines 29-30 in the _january_extraction_example.py_ file), I obtained a __mean reduction of 16.50 %__ of the null values for the extraction of the number of pages, as we can see from the last column:

![](/images/decrease_percentage.png)

Nevertheless, the percentage of null values remains still high, especially when compared to the percentages relating to the extraction of the author and the publishing house (second and third column, respectively). This is due to the presence, in the dataset, of other elements besides books (e.g. movies, CDs, etc.) which do not include the attribute _number of pages_.

The next step will therefore be to identify the different categories of objects present and extrapolate only the _book_ objects. 
Please refer to the lines 14-15 of the _january_extraction_example.py_ file, where the book tag _LM_ was taken from the metadata included in the dataset.

Finally, I created a single dataframe for the entire month containing the information relating to the book object and necessary for subsequent analysis 
(please refer to lines 53-63 of the _january_extraction_example.py_ file).

After adapting the script for each month of the year, I merged the resulting 12 dataframes into a single one for the whole year (please refer to the
_df_merging.py_ file). The dimension of the new dataframe is of 250946 rows and now we can finally start with the exploration of the dataset!

## Exploring the data
Let's first check for possible outliers for the _Eta'_utente_movimento_ (user age) attribute. From the following boxplot we can see the presence of
some outliers (13):

![](/images/outliers.png)

After cleaning the 13 outliers, let's redo the boxplot for further verification:

![](/images/outliers_cleaned.png)

The new dataframe will now have a size of 250933 rows.

Now let's see the types of users who borrow books. From the following bar chart, we can see how the majority of users belong to _BIBLIOTECA SOL_ type, 
corresponding to 23.67% of the total users:

![](/images/users.png)

This typology indicates the inter-systemic loans made between libraries, therefore __we can think of investigating this aspect to understand if and how 
loans between libraries could be optimized, in order to reduce waiting times for users and save shipments between libraries__.
A direct consequence of this analysis could therefore be to understand how to better distribute the titles among the various libraries of the city. 


__To be continued...__
