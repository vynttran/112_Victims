import pyttsx3
import string

def speak(kosSpeak):
    response= kosSpeak
    text = response
    sentences=[]
    res=""
    for char in text:
        if char in string.punctuation:
            sentences.append (res)
            res=""
        else:
            res+=char
    sentences.append (res)	
    converter = pyttsx3.init()
    voice_id = "com.apple.speech.synthesis.voice.xander"

    # Use female voice
    converter.setProperty('voice', voice_id)
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 0.7) #0-1

    for line in sentences:
        converter.say(line)

    converter.runAndWait()
    sentences=[]