import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import seaborn as sns
from transformers import pipeline
import sys
from io import StringIO

sns.set()
import nltk
import re
import string

nltk.download('stopwords')
from nltk.corpus import stopwords


def remove_stopwords(text):
    stop = set(stopwords.words("english"))
    filtered_words = [word.lower() for word in text.split() if word.lower() not in stop]
    return " ".join(filtered_words)


def remove_URL(text):
    url = re.compile(r"https?://\S+|www\.\S+")
    return url.sub(r"", text)


def remove_punct(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


class TextClassificationEmotions:

    def __init__(self):
        self.emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
        self.categories = {'happy': 'p1', 'sadness': 'p2', 'anger': 'p3', 'love': 'p4', 'surprise': 'p5',
                           'fear': 'p6', 'joy': 'p1', 'neutral': 'p7', 'desire': 'p4', 'approval': 'p1',
                           'remorse': 'p2','confusion':'p2','amusement':'p1','optimism':'p1',
                           'nervousness':'p3','excitement':'p1','disapproval':'p3','gratitude':'p1','curiosity':'p5'}

    def get_emotion_label(self, text):
        emotion = self.emotion(text)[0]['label']
        if self.categories.get(emotion, -1) == -1:
            print(emotion)
            return self.categories['neutral']
        return self.categories[emotion]

