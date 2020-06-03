# Changelogs

### 0.0.10 - 0.0.12

- Update module `model`
    - def `visualize_training`
        > Updated some scripts
- Update module `scaling`
    - def `min_max_scaler`
        > Updated conditional `fit_from_data` in `if` statement
    - def `standart_scaler`
        > Updated conditional `fit_from_data` in `if` statement

### 0.0.9

- Update `README.md`
- Update module `model`
    - def `visualize_training`
        > Add label x-axis & y-axis to plot figure

### 0.0.8

- Update module `model`
    - def `visualize_training`
        > Update logical process

### 0.0.7
- Update module `model`
    - def `visualize_training`
        > Argument `output_file=None` is now disabled, use (`acc_output_file=None`, `loss_output_file=None`) instead.
        
        > Add new argument `metrics=('acc', 'loss')`. Support for keras's metrics.

### 0.0.6
- Add new module `audio_processing`
    - def `get_audio_duration`
    - def `reduce_noise`
    - def `trim_silence`
    - def `trim_audio`
- Add new module `text_processing`
    - def `remove_numbers`
    - def `remove_punctuations`
    - def `remove_stopwords`
    - def `clean_text`
    - def `stemming`
- Add new module `scaling`
    - def `min_max_scaler`
    - def `standart_scaler`
  
### 0.0.5
- Update module `cnn`
    > Update logical process
- Update module `confusion_matrix`
    > Update logical process
- Update module `image_extraction`
    > Update logical process

### 0.0.4
- Initial release
- Add new module `audio_extraction`
    - def `extract_pisr`
- Add new module `audio_to_image`
    - def `pitch_figure`
    - def `intensity_figure`
- Add new module `audio_to_text`
    - def `transcript_from_file`
- Add new module `cnn`
    - def `cnn_audio_image_1`
- Add new module `confusion_matrix`
    - def `calc_cm`
- Add new module `image_extraction`
    - def `extract_to_array`
- Add new module `image_processing`
    - def `combine_and_save`
    - def `resize_and_save`
- Add new module `model`
    - def `visualize_training`
- Add new module `text_tokenizer`
    - def `tokenize`
    - def `tokenize_from_csv`

### 0.0.1 - 0.0.3
- Test release