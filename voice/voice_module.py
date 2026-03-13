from gtts import gTTS


def make_voice(text):

    file = "static/voice.mp3"

    tts = gTTS(text)

    tts.save(file)

    return file