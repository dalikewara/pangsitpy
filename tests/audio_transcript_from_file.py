import os
from pangsitpy.audio_to_text import transcript_from_file

source_file = os.path.join(os.path.dirname(__file__), 'files/audio.wav')
transcribbed = transcript_from_file(source_file)
print(transcribbed)
print('=====')
transcribbed = transcript_from_file(source_file, lang='id-ID')
print(transcribbed)
