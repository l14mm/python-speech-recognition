import speech_recognition as sr
import time
from datetime import datetime

def callback(recognizer, audio):
    try:
        timestamp = datetime.now()
        text = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
        
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

        with open("text2speed-results.txt", "a") as f:
            f.write(f'{timestamp} - {text}\n')

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    r = sr.Recognizer()
    m = sr.Microphone()
    
    stop_listening = r.listen_in_background(m, callback)

    time.sleep(30)

    stop_listening(wait_for_stop=False)
    