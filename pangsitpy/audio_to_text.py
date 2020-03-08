import speech_recognition as sr


def transcript_from_file(source_file, lang='en-EN', engine='google-api'):
    r = sr.Recognizer()
    file_source = sr.AudioFile(source_file)
    with file_source as source:
        audio = r.record(source)
    if engine == 'google-api':
        text = r.recognize_google(audio, language=lang)
    else:
        text = r.recognize_google(audio, language=lang)
    return text
