import speech_recognition as sr

if __name__ == "__main__":
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Say something')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('error')