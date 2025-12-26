# -*- coding: utf-8 -*-
"""## Installing & importing necessary packages
"""

!pip install pandas
!pip install bs4
!pip install requests

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

"""## Fetching HTML content for Sample Data

Extracting HTML data and also verifying if it does have data of 100 books.
"""

url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.content, 'html.parser')
sample_book_data = soup.find_all('tr', itemtype= 'http://schema.org/Book')

print(len(sample_book_data))

"""## Sample Data Extraction

Scraping first page as sample & previewing it.
"""

sample_book_list = []

for book in sample_book_data:
    if book.find('td', width= '100%') is not None:
        title = book.find('a', class_= 'bookTitle').text.strip()
        author = book.find('a', class_= 'authorName').text.strip()
        ratings = book.find('span', class_= 'greyText smallText uitext').text.strip()
        score = book.find('span', class_= 'smallText uitext').text.strip()

    sample_book_list.append({'Title': title, 'Author': author, 'Ratings': ratings, 'Scores': score})

sample_df = pd.DataFrame(sample_book_list)
print(sample_df.head(10))

"""## Data Extraction

Scraping the whole data of 100 pages using for loop, basic error handling & also waiting for 5 seconds after each loop, then appending the data to a list called 'book_list' before inserting it into the DataFrame.
"""

book_list = []

page = 1
for page in range(1, 101):
    url = f'https://www.goodreads.com/list/show/1.Best_Books_Ever?page={page}'
    try:
        response = requests.get(url, headers= headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        book_data = soup.find_all('tr', itemtype= 'http://schema.org/Book')

        for book in book_data:
            if book.find('td', width= '100%') is not None:
                title = book.find('a', class_= 'bookTitle').text.strip()
                author = book.find('a', class_= 'authorName').text.strip()
                ratings = book.find('span', class_= 'greyText smallText uitext').text.strip()
                score = book.find('span', class_= 'smallText uitext').text.strip()

            book_list.append({'Title': title, 'Author': author, 'Ratings': ratings, 'Scores': score})

    except requests.exceptions.RequestException as exc:
        print(f"Error fetching page {page}: {exc}")
    time.sleep(5)

df = pd.DataFrame(book_list)
print(len(df))

"""## Data Preview

Duplicating the original DataFrame as a backup & previewing new DataFrame, 'dup_df'
"""

dup_df = df.copy()
print(dup_df.head(10))

"""## Data Cleanup

Cleaning the 'Title' column by removing double quotes and trimming.
"""

dup_df['Title'] = dup_df['Title'].str.replace('"', '', regex = False).str.strip()

"""Removing unnecassary strings from the 'Ratings' column."""

dup_df['Ratings'] = (dup_df['Ratings'] \
                    .str.replace('really liked it ', '', regex= False) \
                    .str.replace('it was amazing ', '', regex= False))

"""Creating two new columns, 'Avg_Ratings' & 'Total_Ratings' by splitting 'Ratings' column."""

dup_df['Avg_Rating'] = dup_df['Ratings'].str.split().str[0]
dup_df['Total_Ratings'] = dup_df['Ratings'].str.split().str[4]

"""Creating two more columns, 'Score' & 'Votes' by splitting 'Scores' column."""

dup_df['Score'] = dup_df['Scores'].str.split().str[1]
dup_df['Votes'] = dup_df['Scores'].str.split().str[3]

"""Dropping columns, 'Ratings' & 'Scores' since its data is already splitted & stored."""

dup_df.drop(columns= ['Ratings', 'Scores'], inplace= True)
dup_df.head()

"""Setting appropriate data types for numeric columns as well as removing ','."""

dup_df['Avg_Rating'] = dup_df['Avg_Rating'].astype('float')
dup_df['Total_Ratings'] = dup_df['Total_Ratings'].str.replace(',', '').astype('int')
dup_df['Score'] = dup_df['Score'].str.replace(',', '').astype('int')
dup_df['Votes'] = dup_df['Votes'].str.replace(',', '').astype('int')

print(dup_df.dtypes)

"""## Cleaned DataFrame

Creating new df, 'cleaned_df' as a cleaned, finished & organised output.
"""

cleaned_df = dup_df[['Title', 'Author', 'Avg_Rating', 'Total_Ratings', 'Votes', 'Score']].copy()

"""## Final Output

This is the final cleaned DataFrame.
"""

print(cleaned_df)

"""## Exporting as CSV File

Exporting the output DataFrame, 'cleaned_df' as a .csv file named 'best_books_ever.csv'.
"""

cleaned_df.to_csv('best_books_ever.csv', index= False, encoding= 'utf-8')
print("Successfully created 'best_books_ever.csv'")