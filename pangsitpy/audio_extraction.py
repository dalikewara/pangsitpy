import os
import parselmouth
import numpy as np
from parselmouth.praat import run_file

praat_sourcerun = os.path.join(os.path.dirname(__file__), 'praat/myspsolution.praat')
temp_dir = os.path.join(os.path.dirname(__file__), '../.temp')


def extract_pisr(source_file, praat_sourcerun=praat_sourcerun,
                 temp_dir=temp_dir):
    sound = parselmouth.Sound(source_file)
    pitch = sound.to_pitch(pitch_ceiling=500.0)
    pitch_values = pitch.selected_array['frequency']
    fltrpitch = list(filter(lambda a: a != 0, pitch_values))
    min_pitch = min(fltrpitch)
    max_pitch = max(pitch_values)
    mean_pitch = sum(fltrpitch) / len(fltrpitch)
    std_pitch = np.std(fltrpitch, ddof=1)
    range_pitch = max_pitch - min_pitch
    intensity = sound.to_intensity(minimum_pitch=100.0)
    intensity_values = intensity.values
    fltrintensity = list(filter(lambda a: a != 0, intensity_values[0]))
    min_intensity = min(fltrintensity)
    max_intensity = max(intensity_values[0])
    mean_intensity = sound.get_intensity()
    std_intensity = np.std(fltrintensity, ddof=1)
    range_intensity = max_intensity - min_intensity
    try:
        os.makedirs(temp_dir, exist_ok=True)
        objects = run_file(praat_sourcerun, -20, 2, 0.3, "yes",
                           source_file, temp_dir, 80, 400, 0.01,
                           capture_output=True)
        print(objects)
        z1 = str(objects[1])
        z2 = z1.strip().split()
        z3 = int(z2[2])
    except:
        z3 = 0
    speaking_rate = z3
    return {
        'sound': sound,
        'pitch': pitch,
        'pitch_values': pitch_values,
        'fltrpitch': fltrpitch,
        'min_pitch': min_pitch,
        'max_pitch': max_pitch,
        'mean_pitch': mean_pitch,
        'std_pitch': std_pitch,
        'range_pitch': range_pitch,
        'intensity': intensity,
        'intensity_values': intensity_values,
        'fltrintensity': fltrintensity,
        'max_intensity': max_intensity,
        'min_intensity': min_intensity,
        'mean_intensity': mean_intensity,
        'std_intensity': std_intensity,
        'range_intensity': range_intensity,
        'speaking_rate': speaking_rate
    }
