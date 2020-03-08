import os
from pangsitpy.audio_extraction import extract_pisr

source_file = os.path.join(os.path.dirname(__file__), 'files/audio.wav')
audio_feature = extract_pisr(source_file)
print(audio_feature)