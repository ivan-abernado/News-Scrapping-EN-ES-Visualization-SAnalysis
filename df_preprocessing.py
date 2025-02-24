import spacy
import pandas as pd
from pandas import DataFrame
from tqdm import tqdm

# Spanish Texts Preprocess for Sentiment Analysis
def spanish_preprocess_light(df_input: DataFrame):
    #Nested function that contains the actual preprocess procedures
    def preprocessor_es(x: str):
        # Every news article's text will be passed on as a Spacy object to preprocess
        doc = nlp(x)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.text.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of Spanish texts, we load a Spanish LLM
    nlp = spacy.load('es_core_news_sm')
    tqdm.pandas(desc='Preprocessing Spanish texts', colour='blue')
    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell

    df_input['Light Prep.'] = df_input['Text'].progress_apply(
        lambda x: preprocessor_es(x)
    )

# Spanish Texts Preprocess for WordCloud plotting or POS/NER Tagging
def spanish_preprocess_deep(df_input: DataFrame):
    # Nested function that contains the actual preprocess procedures
    def preprocessor_es(x: str):
        # Every news article's text will be passed on as a Spacy object to preprocess
        doc = nlp(x)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.lemma_.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of Spanish texts, we load a Spanish LLM
    nlp = spacy.load('es_core_news_sm')
    tqdm.pandas(desc='Preprocessing Spanish texts', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df_input['Deep Prep.'] = df_input['Text'].progress_apply(
        lambda x: preprocessor_es(x)
    )

# English Texts Preprocess for Sentiment Analysis
def english_preprocess_light(df_input: DataFrame):
    # Nested function that contains the actual preprocess procedures
    def preprocessor_en(x: str):
        # Before proceeding with the same preprocess we have done before,
        # we first remove all contractions within the text (e.g., "isn't", "you're", "haven't", etc.)
        # Dictionary with all contractions and what to replace it with
        contractions = {
            "shan't": 'shall not',  # we put this first because this 'sha' wouldn't mean anything
            "n't": ' not',
            "'re": ' are',
            "'m": ' am',
            "'s": '',  # since it can mean either is, has or possession, it's better to outright remove it
            "'ve": ' have',
            "'ll": ' will',
            "'d": ' would'
        }
        words = x.split()

        # List comprehension that swaps all contractions with their non-contracted equivalent
        words_without_contractions = [contractions[word] if word in contractions else word for word in words]
        text = ' '.join(words_without_contractions)

        # Now we convert the text into a Spacy object
        doc = nlp(text)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.text.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of English texts, we load an English LLM
    nlp = spacy.load('en_core_web_sm')
    tqdm.pandas(desc='Preprocessing English texts', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df_input['Light Prep.'] = df_input['Text'].progress_apply(
        lambda x: preprocessor_en(x)
    )

# English Texts Preprocess for WordCloud plotting or POS/NER Tagging
def english_preprocess_deep(df_input: DataFrame):
    # Nested function that contains the actual preprocess procedures
    def preprocessor_en(x: str):
        # Before proceeding with the same preprocess we have done before,
        # we first remove all contractions within the text (e.g., "isn't", "you're", "haven't", etc.)
        # Dictionary with all contractions and what to replace it with
        contractions = {
            "shan't": 'shall not',  # we put this first because this 'sha' wouldn't mean anything
            "n't": ' not',
            "'re": ' are',
            "'m": ' am',
            "'s": '',  # since it can mean either is, has or possession, it's better to outright remove it
            "'ve": ' have',
            "'ll": ' will',
            "'d": ' would'
        }
        words = x.split()

        # List comprehension that swaps all contractions with their non-contracted equivalent
        words_without_contractions = [contractions[word] if word in contractions else word for word in words]
        text = ' '.join(words_without_contractions)

        # Now we convert the text into a Spacy object
        doc = nlp(text)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.lemma_.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of English texts, we load an English LLM
    nlp = spacy.load('en_core_web_sm')
    tqdm.pandas(desc='Preprocessing English texts', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df_input['Deep Prep.'] = df_input['Text'].progress_apply(
        lambda x: preprocessor_en(x)
    )

newspaper = 'rtve'

language = 'ES'

df = pd.read_csv(f'News CSVs/{language.upper()}/{newspaper.lower()}.csv')

spanish_preprocess_light(df)
spanish_preprocess_deep(df)

df.to_csv(f'News CSVs/{language.upper()}/{newspaper.lower()}.csv', mode='w', encoding='utf-8-sig', index=False)
