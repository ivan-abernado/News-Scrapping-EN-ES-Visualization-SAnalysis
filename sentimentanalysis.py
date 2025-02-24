import pandas as pd
from pandas import DataFrame
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from tqdm import tqdm

def sentiment_analysis_es(df_input: DataFrame):
    def polarity_analyzer(x: str):
        doc = nlp(x)

        return doc._.blob.polarity

    def subjectivity_analyzer(x: str):
        doc = nlp(x)

        return doc._.blob.subjectivity

    nlp = spacy.load('es_core_news_sm')

    nlp.add_pipe('spacytextblob')

    tqdm.pandas(desc='Sentiment Analysing Texts (Polarity)', colour='yellow')
    df_input['Sentiment'] = df_input['Light Prep.'].progress_apply(
        lambda x: polarity_analyzer(x)
    )

    tqdm.pandas(desc='Sentiment Analysing Texts (Subjectivity)', colour='yellow')
    df_input['Subjectivity'] = df_input['Light Prep.'].progress_apply(
        lambda x: subjectivity_analyzer(x)
    )

def sentiment_analysis_en(df_input: DataFrame):
    def polarity_analyzer(x: str):
        doc = nlp(x)

        return doc._.blob.polarity

    def subjectivity_analyzer(x: str):
        doc = nlp(x)

        return doc._.blob.subjectivity

    nlp = spacy.load('en_core_web_sm')

    nlp.add_pipe('spacytextblob')

    tqdm.pandas(desc='Sentiment Analysing Texts (Polarity)', colour='yellow')
    df_input['Sentiment'] = df_input['Light Prep.'].progress_apply(
        lambda x: polarity_analyzer(x)
    )

    tqdm.pandas(desc='Sentiment Analysing Texts (Subjectivity)', colour='yellow')
    df_input['Subjectivity'] = df_input['Light Prep.'].progress_apply(
        lambda x: subjectivity_analyzer(x)
    )

newspaper = 'elperiodico'

language = 'ES'

df = pd.read_csv(f'News CSVs/{language.upper()}/{newspaper.lower()}.csv')

sentiment_analysis_es(df)

df.to_csv(f'News CSVs/{language.upper()}/{newspaper.lower()}.csv', mode='w', encoding='utf-8-sig', index=False)