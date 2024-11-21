import subprocess as cmdLine
import speech_recognition as sr
import ollama


#clase que traduce voz a texto
class reconocevoz:
    def __init__(self):
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            self.r.pause_threshold = 0.9 # debe detener automaticamente la grabacion
            self.r.energy_threshold = 600
            print ("hable ahora : ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language="es")
                return text
               
                #print(text)              
            except:
                return None




class eSpeak:

    #__init__ definimos voces
    def __init__(self, voz='mb-vz1'):
        self.voz = voz

    # dice el texto
    def decir(self, ctext):
        # define la linea de comando
        command = 'espeak -v ' + self.voz + " " + chr(34) + ctext + chr(34)
        # ejecuta comando en la terminal
        print(command)
        result = cmdLine.run(command, shell=True, capture_output=True, text=True)

       



