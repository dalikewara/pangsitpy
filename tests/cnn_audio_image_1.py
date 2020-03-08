import os
from pangsitpy.cnn import cnn_audio_image_1

model = cnn_audio_image_1(audio_shape=(1, 15), image_shape=(64, 64, 1), total_labels=8,
                          plot_to_file=None, optimizer=None, loss=None,
                          metrics=None)
print(model)
print('=====')
temp_dir = os.path.join(os.path.dirname(__file__), '../.temp')
plot_to_file = temp_dir + '/cnn_audio_image_1.figure.png'
model = cnn_audio_image_1(audio_shape=(1, 15), image_shape=(64, 64, 1), total_labels=8,
                          plot_to_file=plot_to_file, optimizer=None, loss=None,
                          metrics=None)
print(model)