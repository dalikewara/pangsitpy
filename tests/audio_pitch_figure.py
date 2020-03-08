import os
from pangsitpy.audio_to_image import pitch_figure

source_file = os.path.join(os.path.dirname(__file__), 'files/audio.wav')
pitch_figure(source_file)
print('=====')
temp_dir = os.path.join(os.path.dirname(__file__), '../.temp')
output_file = temp_dir + '/audio.pitch.png'
os.makedirs(temp_dir, exist_ok=True)
pitch_figure(source_file, output_file=output_file)