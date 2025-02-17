import spacy
from pandas import DataFrame
from tqdm import tqdm

#Preprocess for Sentiment Analysis with Texts in Spanish
def spanish_preprocess_light(df: DataFrame):
    #Nested function that contains the actual preprocess procedures
    def preprocessor_es(x: str):
        # Every news article's text will be passed on as an Spacy object to preprocess
        doc = nlp(x)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.text.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of Spanish texts, we load an Spanish LLM
    nlp = spacy.load('es_core_news_sm')
    tqdm.pandas(desc='Preprocessing Spanish text', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df['Text'] = df['Text'].progress_apply(
        lambda x: preprocessor_es(x)
    )

#Preprocess for WordCloud plotting with Texts in Spanish
def spanish_preprocess_deep(df: DataFrame):
    # Nested function that contains the actual preprocess procedures
    def preprocessor_es(x: str):
        # Every news article's text will be passed on as an Spacy object to preprocess
        doc = nlp(x)

        # List comprehension for the preprocess of tokens within the text.
        # The preprocess removes stopwords and punctuation
        cleaned_words = [
            token.lemma_.lower() for token in doc
            if not token.is_stop and not token.is_punct
        ]
        cleaned_text = ' '.join(cleaned_words)

        return cleaned_text

    # Since this is the function for the preprocess of Spanish texts, we load an Spanish LLM
    nlp = spacy.load('es_core_news_sm')
    tqdm.pandas(desc='Preprocessing Spanish text', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df['Text'] = df['Text'].progress_apply(
        lambda x: preprocessor_es(x)
    )

#Preprocess for Sentiment Analysis with Texts in English
def english_preprocess_light(df: DataFrame):
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

        # Now we convert the text into an Spacy object
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
    tqdm.pandas(desc='Preprocessing English text', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df['Text'] = df['Text'].progress_apply(
        lambda x: preprocessor_en(x)
    )

#Preprocess for WordCloud plotting with Texts in English
def english_preprocess_deep(df: DataFrame):
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

        # Now we convert the text into an Spacy object
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
    tqdm.pandas(desc='Preprocessing English text', colour='blue')

    # We apply a lambda function to preprocess each Text cell within the news dataframe
    # and overwrite that same cell
    df['Text'] = df['Text'].progress_apply(
        lambda x: preprocessor_en(x)
    )