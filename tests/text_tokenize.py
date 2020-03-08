from pangsitpy.text_tokenizer import tokenize

fit_data = [
    'Ini adalah contoh text',
    'Sama dengan yang diatas',
    'Yang ini juga merupakan sebuah contoh text'
]
text_sequences = tokenize(fit_data)
print(text_sequences)
print('=====')
text_sequence = tokenize(fit_data, text_to_sequence='Saya ini adalah manusia')
print(text_sequence)