import pandas as pd
from keras.preprocessing.text import Tokenizer


def tokenize(fit_data, num_words=5000000,
             text_to_sequence=None):
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(fit_data)
    sequences = tokenizer.texts_to_sequences(fit_data)
    vocab_size = len(tokenizer.word_index) + 1
    sequence = None
    if text_to_sequence:
        sequence = tokenizer.texts_to_sequences([text_to_sequence])
    return {
        "sequence": sequence,
        "sequences": sequences,
        "vocab_size": vocab_size
    }


def tokenize_from_csv(source_file, text_column, num_words=5000000,
                      text_to_sequence=None):
    df = pd.read_csv(source_file, engine='python', encoding='latin-1',
                     skipinitialspace=True)
    fit_data = df[text_column].values
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(fit_data)
    sequences = tokenizer.texts_to_sequences(fit_data)
    vocab_size = len(tokenizer.word_index) + 1
    sequence = None
    if text_to_sequence:
        sequence = tokenizer.texts_to_sequences([text_to_sequence])
    return {
        "sequence": sequence,
        "sequences": sequences,
        "vocab_size": vocab_size
    }
