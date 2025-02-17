import newspaper
import pandas as pd
import re
from tqdm import tqdm

# This function scrapes whatever website we pass to it with the library newspaper
# and saves all news into a .csv file
def scrapping(web_domain: str) -> None:
    # We especify which website we want to scrape
    url = f'https://{web_domain}/'

    website = newspaper.build(url)

    # List to which we will add all news.
    article_list = []

    # For loop for every article
    for article in tqdm(website.articles, desc=f'Scrapping news from {web_domain}', colour='blue'):

        # try-except function that will handle client erros like 403 or 404
        try:
            article.download()
            article.parse()

            # try-except function that handles None values or dates in other formats
            try:
                 # This regex pattern tries to match dates in formats similar to YYYY-MM-DD
                date = re.search(r'(\d+)-(\d+)-(\d+)\b', str(article.publish_date)).group()
            except AttributeError:
                date = article.publish_date

            # Dictionary with the article's info that we will add to our previous list
            article_data = {
                'Title': article.title,
                'Text': article.text,
                'Date': date,
                'Url': article.source_url
            }
            article_list.append(article_data)

        except newspaper.article.ArticleException as e:
            print(f'Error {e}, the scrapping will stop.')
            break

    pd.set_option('display.max_columns', None)

    # We convert the list into a DataFrame and then we save it as a .csv file
    df = pd.DataFrame(article_list)

    df.to_csv(f'{web_domain}.csv', mode='w', encoding='utf-8-sig', index=False)