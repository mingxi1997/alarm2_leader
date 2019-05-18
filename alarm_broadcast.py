#!/usr/bin/python3
# coding: utf-8

import subprocess
import time




def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()
    
def afirm_broad():
    with open('terse_affirm.txt','r')as f:
        terse_affirm=eval(f.read())
    if sum(terse_affirm)>0:
        
        playsound('becareful.mp3')
        
        for i in range(len(terse_affirm)):
            if terse_affirm[i]==1:
                playsound('u'+str(i+1)+'.mp3')
                
        
        playsound('receive_alarm.mp3')
        playsound('alarm.mp3')
     
         
while True:
    try:
        afirm_broad()
        time.sleep(2)
    except:
        pass
     