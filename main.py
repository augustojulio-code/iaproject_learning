import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executaComando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Robo' in comando:
                comando = comando.replace('Robo', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print("Microfone não esta ok")

    return comando


def comandoVoiceUser():
    comando = executaComando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procurar' in comando:
        procure = comando.replace('procurar', ' ')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(procure, 2)
        print(result)
        maquina.say(result)
        maquina.runAndWait()


comandoVoiceUser()
