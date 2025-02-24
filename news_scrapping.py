import newspaper
import pandas as pd
import re
import os
from tqdm import tqdm

# This function scrapes whatever website we pass to it with the library newspaper
# and saves all news into a .csv file
def scrapping(web_domain: str, language_code: str) -> None:
    # We specify which website we want to scrape
    url = f'https://{web_domain.lower()}'

    # Now we overwrite the web_domain variable, so that the resulting csv
    # will be saved with an apropiate name (e.g., 'nytimes.csv' instead of 'nytimes.com.csv'
    web_domain = re.search(r'^(\w+)', web_domain).group()

    website = newspaper.build(url, language=f'{language_code.lower()}')

    # List to which we will add all news.
    article_list = []

    # For loop for every article
    for article in tqdm(website.articles, desc=f'Scrapping news from {web_domain}', colour='blue'):

        # try-except function that will handle client erros like 403 or 404
        try:
            article.download()
            article.parse()

            # If article's title and text exist/are not missing values...
            if article.title and article.text:
                # try-except function that handles None values or dates in other formats
                try:
                     # This regex pattern tries to match dates in formats similar to YYYY-MM-DD
                    date = re.search(r'(\d+)-(\d+)-(\d+)\b', str(article.publish_date)).group()
                except AttributeError:
                    date = article.publish_date

                # Dictionary with the article's info that we will add to our previous list
                article_data = {
                    'Source': web_domain.upper(),
                    'Date': date,
                    'Title': article.title,
                    'Text': article.text
                }
                article_list.append(article_data)
            else:
                print('\nArticle skipped due to missing values (NaN)')

        except newspaper.article.ArticleException as e:
            print(f'Error {e}. The scrapping will stop. The already scrapped news will still be saved.')
            break

    pd.set_option('display.max_columns', None)

    # We convert the list into a DataFrame and drop any missing values (NaN),
    # which will make it foolproof for the future
    df = pd.DataFrame(article_list)
    df = df.dropna()

    # Ensure the 'CSVs' folder exists, create it if it doesn't
    os.makedirs(f'News CSVs/{language_code.upper()}', exist_ok=True)

    # Finally, we save the dataframe into a .csv file
    df.to_csv(f'News CSVs/{language_code.upper()}/{web_domain.lower()}.csv', mode='w', encoding='utf-8-sig', index=False)


# We specify from which newspaper we want to scrap news from
# Note: Write the newspaper's domain
news_website = 'elespanol.es'

# We specify the language in which we want to scrap news in.
# This serves two purposes:
# -First, it allows us to scrap news from websites in multiple languages (for example, HuffPost)
# -Second, it allows us to automatically save the final .csv file into its respective folder
language = 'ES'

scrapping(news_website, language)
