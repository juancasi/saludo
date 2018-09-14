#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:38:33 2018

@author: juancastro
"""
"""
from gtts import gTTS
mensaje = "Buenos dias"
tts = gTTS(mensaje, lang="es")
tts.save('hello03.mp3')
"""

"""
from pymongo import MongoClient
client = MongoClient()
db = client['saludo']
collection = db['saludos']
data = collection.find_one({"language": "fr"})
print(type(data))
print(data)

gm = data["GM"]
ga = data["GA"]
ge = data["GE"]

print("GM", gm)
print("GA", ga)
print("GE", ge)
"""


from pyknow import *

class Greeting(Fact):
    pass

class Hora(Fact):
    pass

class Saludar(KnowledgeEngine):
    greeting = ""
    salution = ""
    
    def setGreeting(self, g):
        self.greeting = g
    
    def getGreeting(self):
        return self.greeting
        
    def getMessage(self):
        return self.getGreeting()
    

    @Rule(Greeting(hora = P(lambda hora: hora >= 0) & P(lambda hora: hora <= 11)))
    def morning(self):
        self.setGreeting("GM")

    @Rule(Greeting(hora = P(lambda hora: hora >= 12) & P(lambda hora: hora <= 17)))
    def afternoon(self):
        self.setGreeting("GA")
        
    @Rule(Greeting(hora = P(lambda hora: hora >= 18) & P(lambda hora: hora <= 23)))
    def evening(self):
        self.setGreeting("GE")
        
        
watch('RULES', 'FACTS')
nxm = Saludar()  
nxm.reset()


for i in range(0,24):
    print(i)
    nxm.declare(Greeting(hora=i))
    nxm.run()
    #nxm.facts      
    message = nxm.getMessage()
    print(message)
    
    



