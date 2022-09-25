import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
# import seaborn as sns
# sns.set()
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


class TextClassificationWeb:

    def __init__(self):
        self.model = None
        df = self.fit()
        self.train_model(df)
        self.categories = {'chrono': 'p1', 'arial': 'p2', 'muli': 'p3', 'merriweather': 'p4', 'open sans': 'p5',
                           'times': 'p6', 'helvetica': 'p7', 'proxima': 'p8'}

    def fit(self):
        df = pd.read_csv('rawData.csv')
        # Organize  data
        del df['trash']
        del df['num']
        df = df.dropna()
        df['Font'] = df['Font'].str.lower().str.replace('"', '')
        df['Text'] = df['Text'].str.lower().str.replace('"', '')
        df.applymap(lambda x: x.replace('"', ''))
        df['count'] = df['Text'].str.lower().str.split().str.len()
        df = df[df['count'] > 2]
        df.replace(to_replace=[r"\\t|\\n|\\r\\", "\t|\n|\r|"], value=["", ""], regex=True, inplace=True)
        categories = ['chrono', 'arial', 'muli', 'merriweather', 'open sans', 'times', 'helvetica', 'proxima']
        df['font'] = np.where(df['Font'].str.contains('chrono'), 'chrono', df['Font'])
        for i in categories:
            df['font'] = np.where(df['Font'].str.contains(i), i, df['font'])

        # Delete  uncommon fonts
        df = df.sort_values(by=['count'], ascending=False)
        del df['Font']
        df = df.where(df['font'].isin(categories)).dropna()
        df["Text"] = df.Text.map(remove_URL)
        df["Text"] = df.Text.map(remove_punct)
        df["Text"] = df.Text.map(remove_stopwords)
        return df

    def train_model(self, df: pd.DataFrame):
        x_train, x_test, y_train, y_test = train_test_split(df['Text'], df['font'], test_size=0.3, random_state=7)
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(x_train, y_train)

    def predict(self, data):
        d_s = pd.Series(data)
        pred = self.model.predict(d_s)[0]
        return self.categories[pred]



