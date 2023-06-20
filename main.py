
import pyttsx3
import speech_recognition as sr
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executaComando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz=audio.listen(source)
            comando=audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print("Microfone não esta ok")

    return comando

def comandoVoiceUser():
    comando = executaComando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são'+hora)
        maquina.runAndWait()


comandoVoiceUser()