import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def remove_numbers(text):
    return re.sub(r'\d+', '', text)


def remove_punctuations(text):
    text = text.strip()
    text = re.sub('[\W_]+', ' ', text)
    return text.translate(str.maketrans('', ''))


def remove_stopwords(text, lang='en-EN'):
    if lang == 'id-ID':
        factory = StopWordRemoverFactory()
        stopword = factory.create_stop_word_remover()
        return stopword.remove(text)
    return text


def clean_text(text):
    text = re.sub('@[a-z0-9]+|rt user|RT USER|retweet|RETWEET|user|USER|korsa|KORSA|ppp|PPP|ð', '', text)
    return re.sub('[\W_]+', ' ', text)


def stemming(text, lang='en-EN'):
    if lang == 'id-ID':
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return stemmer.stem(text)
    return text
