import gtts
from gtts import gTTS
from playsound import playsound
language = ['en','hi']
txt = ["यह हिंदी में एक उदाहरण है", "This is an example"]
english_txt = "This is an example"
for i in language:
    print(i)
    if i == 'en':
        sound1 = gtts.gTTS(text = txt[1], lang = i, slow = False)
        sound1.save("welcome_eng.mp3")
        playsound("welcome_eng.mp3")
    elif i == 'hi':
        sound1 = gtts.gTTS(text = txt[0], lang = i, slow = False)
        sound1.save("welcome_hin.mp3")
        playsound("welcome_hin.mp3")