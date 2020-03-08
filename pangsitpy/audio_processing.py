import librosa
from logmmse import logmmse_from_file
from pydub import AudioSegment


def get_audio_duration(source_file):
    return librosa.get_duration(filename=source_file)


def reduce_noise(source_file, output_file=None, initial_noise=30,
                 window_size=0, noise_threshold=0.15):
    logmmse_from_file(source_file, output_file=(output_file or source_file), initial_noise=initial_noise,
                      window_size=window_size, noise_threshold=noise_threshold)


def trim_silence(source_file, output_file=None):
    y, sr = librosa.load(source_file)
    yt, index = librosa.effects.trim(y)
    librosa.output.write_wav((output_file or source_file), yt, sr)


def trim_audio(source_file, trim_duration=0, output_file=None,
               extension='wav'):
    if output_file:
        output_file = output_file
    else:
        output_file = source_file
    if trim_duration > 0:
        ad = AudioSegment.from_wav(source_file)
        duration = round(get_audio_duration(source_file))
        st = 0 * 1000
        ed = trim_duration * 1000
        div = round(duration / trim_duration)
        if div <= 1:
            f_trim_sec = ad[st:ed]
            f_trim_sec.export(output_file + '.trim-1.' + extension, format=extension)
        else:
            for i in range(1, div + 1):
                f_trim_sec = ad[st:ed]
                f_trim_sec.export(output_file + '.trim-' + str(i) + '.' + extension, format=extension)
                st = ed
                ed = ed + (trim_duration * 1000)
