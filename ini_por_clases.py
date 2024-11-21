#importamos suprocesos 
import subprocess as cmdLine
import speech_recognition as sr
import ollama
from separa_clases import eSpeak
from separa_clases import reconocevoz





recoce = reconocevoz()
eS = eSpeak()


Corre = True
while Corre:
    text = recoce.recognize()
    stream = ollama.chat(
            model='llama3', 
            messages=[{"role": "user", "content": text},
                      {"role": "assistant", "content": "asistente"}
                      ],
                     format=text, 
                     options={"temperature": 0.1}
            )
    for chunk in stream:
           #print(chunk['message']['content'], flush=True)
            ctext = stream['message']['content']
            #print(bot)       
    eS.decir(ctext)
    
