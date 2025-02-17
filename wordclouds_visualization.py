import pandas as pd
from pandas import DataFrame
#Wordcloud
from wordcloud import WordCloud
#Wordcloud mask
from PIL import Image
import numpy as np
#Plotting
import matplotlib.pyplot as plt

# This function plots the data as a wordcloud. This is wordcloud function for general data
def wordcloud_general(df: DataFrame, web_domain: str):
    # We convert all cells within the 'Text' column to a list object
    list_news = df['Text'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the wordcloud's parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='default'
    ).generate(list_news)

    plt.title(f'Most Frequent N-Grams in {web_domain}\'s Front Page')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for Spanish' websites
def wordcloud_esp_mask(df: DataFrame, web_domain: str):
    # Spain image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures\masks\spain_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df['Text'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the wordcloud's parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='inferno',
        mask=im,
        contour_width = 1
    ).generate(list_news)

    plt.title(f'Most Frequent N-Grams in {web_domain}\'s Front Page')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for English' websites
def wordcloud_uk_mask(df: DataFrame, web_domain: str):
    # UK image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures\masks\uk_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df['Text'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the wordcloud's parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='gist_gray_r',
        mask=im,
        contour_width=1
    ).generate(list_news)

    plt.title(f'Most Frequent N-Grams in {web_domain}\'s Front Page')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for US' websites
def wordcloud_us_mask(df: DataFrame, web_domain: str):
    # US image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures\masks\us_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df['Text'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the wordcloud's parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='seismic_r',
        mask=im,
        contour_width=1
    ).generate(list_news)

    plt.title(f'Most Frequent N-Grams in {web_domain}\'s Front Page')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()