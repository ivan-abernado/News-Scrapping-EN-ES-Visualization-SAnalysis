import pandas as pd
from pandas import DataFrame
# General Plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Wordcloud
from wordcloud import WordCloud
# Wordcloud mask
from PIL import Image
import numpy as np


def scatterplot_subj_polar(df_input: DataFrame, plot_title: str, plot_xlabel: str, plot_ylabel: str):

    # Assuming your DataFrame is df with 'Sentiment' and 'Subjectivity' columns
    plt.figure(figsize=(8, 6))

    # Create a scatter plot
    sns.scatterplot(data=df_input, x='Sentiment', y='Subjectivity', hue='Source', palette='deep')

    # Customize plot
    plt.title(f'{plot_title}', fontsize=16)
    plt.xlabel(f'{plot_xlabel}', fontsize=12)
    plt.ylabel(f'{plot_ylabel}', fontsize=12)
    plt.grid(True)

    # Show the plot
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for general data
def wordcloud_general(df_input: DataFrame, plot_title: str):
    # We convert all cells within the 'Text' column to a list object
    list_news = df_input['Deep Prep.'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the WordCloud parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='default'
    ).generate(list_news)

    plt.title(f'{plot_title}')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for Spanish websites
def wordcloud_esp_mask(df_input: DataFrame, plot_title: str):
    # Spain image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures/masks/spain_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df_input['Deep Prep.'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the WordCloud parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='inferno',
        mask=im,
        contour_width = 1
    ).generate(list_news)

    plt.title(f'{plot_title}')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for English websites
def wordcloud_uk_mask(df_input: DataFrame, plot_title: str):
    # UK image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures/masks/uk_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df_input['Deep Prep.'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the WordCloud parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='bwr_r',
        mask=im,
        contour_width=1
    ).generate(list_news)

    plt.title(f'{plot_title}')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function plots the data as a wordcloud. This is wordcloud function for US' websites
def wordcloud_us_mask(df_input: DataFrame, plot_title: str):
    # US image mask (mask refers to the form the wordcloud will adopt)
    im = np.array(Image.open(r'Figures/masks/us_mask.jpg'))

    # We convert all cells within the 'Text' column to a list object
    list_news = df_input['Deep Prep.'].str.cat(sep=' ')

    # We create the plot's size
    plt.figure(figsize=(10, 8))

    # These are the WordCloud parameters that define its design
    wordcloud = WordCloud(
        max_words=120,
        background_color='white',
        colormap='seismic_r',
        mask=im,
        contour_width=1
    ).generate(list_news)

    plt.title(f'{plot_title}')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# This function quickens the plotting of multiple dataframes,
# since it automatically concatenates them into one.
def concatenate_n_dfs(language_code: str, newspaper1: str, newspaper2: str, newspaper3: str, newspaper4: str) -> DataFrame:
    df1 = pd.read_csv(f'News CSVs/{language_code.upper()}/{newspaper1.lower()}.csv')
    df2 = pd.read_csv(f'News CSVs/{language_code.upper()}/{newspaper2.lower()}.csv')
    df3 = pd.read_csv(f'News CSVs/{language_code.upper()}/{newspaper3.lower()}.csv')
    df4 = pd.read_csv(f'News CSVs/{language_code.upper()}/{newspaper4.lower()}.csv')
    #df5 = pd.read_csv(f'News CSVs/{language_code.upper()}/{newspaper5.lower()}.csv')

    # We concatenate all the dataframes into one,
    # slicing by the first 200 rows to ensure they are of equal size
    dataframes = [df1, df2, df3, df4]
    sliced_dfs = [dataframe[:200] for dataframe in dataframes]
    df_concat = pd.concat(sliced_dfs, ignore_index=True)

    return df_concat

#newspaper = 'abc'
#
#df = pd.read_csv(f'{newspaper}.csv')

language = 'ES'

df = concatenate_n_dfs(language,
                          '20minutos',
                          'elperiodico',
                          'libertaddigital',
                          'rtve')

#wordcloud_esp_mask(df, 'Most Frequent N-Grams - Spanish Newspapers')

scatterplot_subj_polar(df, 'Sentiment vs. Subjectivity Article Scores of Spanish Newspapers',
                       'Sentiment',
                       'Subjectivity')