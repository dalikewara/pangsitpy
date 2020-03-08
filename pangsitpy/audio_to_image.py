import parselmouth
import numpy as np
import matplotlib.pyplot as plt


def pitch_figure(source_file, output_file=None, pitch_ceiling=500.0,
                 maximum_frequency=8000, window_length=0.03):
    sound = parselmouth.Sound(source_file)
    pitch = sound.to_pitch(pitch_ceiling=pitch_ceiling)
    pre_emphasized_snd = sound.copy()
    pre_emphasized_snd.pre_emphasize()
    spectrogram = pre_emphasized_snd.to_spectrogram(window_length=window_length,
                                                    maximum_frequency=maximum_frequency)
    plt.figure()
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - 70, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [Hz]")
    plt.twinx()
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values == 0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("Fundamental frequency [Hz]")
    plt.xlim([sound.xmin, sound.xmax])
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()


def intensity_figure(source_file, output_file=None, minimum_pitch=100.0,
                     window_length=0.03, maximum_frequency=8000):
    sound = parselmouth.Sound(source_file)
    intensity = sound.to_intensity(minimum_pitch=minimum_pitch)
    pre_emphasized_snd = sound.copy()
    pre_emphasized_snd.pre_emphasize()
    spectrogram = pre_emphasized_snd.to_spectrogram(window_length=window_length,
                                                    maximum_frequency=maximum_frequency)
    plt.figure()
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - 70, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [Hz]")
    plt.twinx()
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("Intensity [dB]")
    plt.xlim([sound.xmin, sound.xmax])
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()
