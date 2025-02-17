from news_scrapping import scrapping
from df_preprocessing import spanish_preprocess_deep, english_preprocess_deep
from wordclouds_visualization import wordcloud_esp_mask, wordcloud_us_mask, wordcloud_uk_mask
import pandas as pd

newspaper = 'nytimes.com'

scrapping(newspaper)

df = pd.read_csv(f'{newspaper}.csv')

spanish_preprocess_deep(df)
#english_preprocess_deep(df)

wordcloud_us_mask(df, newspaper)