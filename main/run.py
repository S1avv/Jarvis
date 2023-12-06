from main.distributor import dist_text
import speech_recognition as sr
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4

p = pyaudio.PyAudio()

def record_audio():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


    stream.stop_stream()
    stream.close()

    audio_data = b''.join(frames)
    return audio_data

def recognize_speech(audio_data):
    recognizer = sr.Recognizer()

    audio = sr.AudioData(audio_data, sample_rate=RATE, sample_width=p.get_sample_size(FORMAT))

    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        print("Распознанный текст:", text)
        dist_text(text)
    except sr.UnknownValueError:
        print("Речь не распознана")
    except sr.RequestError as e:
        print("Не удалось получить результаты от службы распознавания речи Google; {0}".format(e))
    finally:
        audio_data = record_audio()
        recognize_speech(audio_data)

if __name__ == "__main__":
    while True:
        audio_data = record_audio()
        recognize_speech(audio_data)
