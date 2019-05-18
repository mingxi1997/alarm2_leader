#!/usr/bin/python3
# coding: utf-8

import time
import subprocess





def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()

with open('key_sound.txt','w')as f:
    f.write('rest')
    
while True:
  try:
    with open('key_sound.txt','r')as f:
        music=f.read()
    with open('key_sound.txt','w')as f:
            f.write('rest')
    if music=='rest':
        time.sleep(2)
    else:
        music_lists=music.split('\n')
        for mu in music_lists:
            if mu=='rest' or mu=='':
                pass
            else:
                playsound(mu)
  except:
      pass

    
        
    





