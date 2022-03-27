# import speech_recognition as s_r
# print(s_r.__version__) # just to print the version not required
# r = s_r.Recognizer()
# my_mic = s_r.Microphone() #my device index is 1, you have to put your device index
# with my_mic as source:
#     print("a")
#     audio = r.listen(source) #take voice input from the microphone
# print(r.recognize_google(audio)) #to print voice into text

# import speech_recognition as sr

# for mic in sr.Microphone.list_microphone_names():
#     print(mic)

# import speech_recognition as sr

# def listen():
#     r = sr.Recognizer()
#     mic = sr.Microphone() 
#     with mic as source:
#         # r.adjust_for_ambient_noise(source) case you ever have noise issues
#         audio = r.listen(source, timeout=10)
#         return r.recognize_google(audio)
# print(listen())

import speech_recognition as fri

listen = fri.Recognizer()

try:
    with fri.Microphone() as cmd:
        print('Waiting...')
        voice = listen.listen(cmd)
        cmdz = listen.recognize_google(voice)
        print(cmdz)
except:
    pass 