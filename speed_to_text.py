import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():
    while True:  # Infinite loop
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText
            
        except sr.RequestError as e:
            print("Could not request results:", e)

        except sr.UnknownValueError:  
            print("Unknown error happened")  
            
    return

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text)
        f.write("\n")

while True:
    text = record_text()
    output_text(text)

    print("Hello World")