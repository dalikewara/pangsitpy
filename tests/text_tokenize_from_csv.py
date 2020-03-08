import os
from pangsitpy.text_tokenizer import tokenize_from_csv

source_file = os.path.join(os.path.dirname(__file__), 'files/text.csv')
text_sequences = tokenize_from_csv(source_file, 'sentence')
print(text_sequences)
print('=====')
text_sequence = tokenize_from_csv(source_file, 'sentence', text_to_sequence='Saya ini adalah manusia')
print(text_sequence)
print(text_sequence['sequence'])