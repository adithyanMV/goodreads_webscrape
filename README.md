# 📚 Goodreads WebScrape

<img width="500" height="200" alt="goodreads_logo" src="https://github.com/user-attachments/assets/5cdead70-b72b-4968-b451-b552c1c1e5a9" />

This repository contains the code I put together to web scrape a list from [Goodreads](https://www.goodreads.com) titled [Best Books Ever](https://www.goodreads.com/list/show/1.Best_Books_Ever), which features 10,000 popular community-voted books. Additionally, it includes the final CSV output containing the scraped data for easy access.

**Note:** GitHub may not render the CSV output due to its large size. The file can still be downloaded for full access.
___

## 🛠 Tools Utilized

This project is fully coded using **Python** and its following packages;

  - **Pandas**: For data cleanup, data manipulation and storage in CSV format.
  - **Requests**: For making HTTP requests.
  - **BeautifulSoup**: For parsing HTML content.
  - **Time**: To incoporate sleep function and to prevent rate limiting.
___

## 📁 Output

The code and scraped data is available here:

  - [goodreads_webscrape.ipynb](goodreads_webscrape.ipynb): Contains the Jupyter notebook.
  - [goodreads_webscrape.py](goodreads_webscrape.py): Contains the Python script.
  - [best_books_ever.csv](best_books_ever.csv): Contains `Title` `Author` `Avg_Rating` `Total_Ratings` `Votes` `Score`
___

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
