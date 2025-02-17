from news_scrapping import scrapping
from df_preprocessing import spanish_preprocess_light, spanish_preprocess_deep, english_preprocess_light, english_preprocess_deep
from wordclouds_visualization import wordcloud_general, wordcloud_esp_mask, wordcloud_us_mask, wordcloud_uk_mask
import pandas as pd

# Load the news website you want to scrape news from. Only write the website's domain
newspaper = 'abc.es'

# Website scrapping. The results will be save as a .csv file with the name of the website (in this example, the file would be 'abc.es.csv')
scrapping(newspaper)

df = pd.read_csv(f'{newspaper}.csv')

# Spanish news preprocessing for wordcloud visualization (for sentiment analysis use the _light version)
spanish_preprocess_deep(df)

# Wordcloud that uses the territory of Spain as a mask
wordcloud_esp_mask(df, newspaper)
