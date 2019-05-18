#!/usr/bin/python3
# coding: utf-8

import requests

import time
import datetime
import os
import subprocess


server='http://192.168.1.4'
def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()
    
units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','阵管防卫连','营区大门岗','家属院门岗','油库','机关楼','装备场区','共同训练场']

def get_command_model():
    command={}
    for unit in units_order:
        command[unit]= {'voice': '0000', 'text': 'BROAD ', 'expand': '', 'command': '0000'}
    command['time']=str(datetime.datetime.now())[:-7]
    return command

def get_recent_command():
    with open('local_command.txt','r')as f:
        command=eval(f.read())
    return command




def command_over():
    with open('command_publish.txt','w')as f:
        f.write('over')
    
    
    
def affirm_alarm():
     data={'key':'19979476','affirm':'all0'}
     requests.post(server+'/affirm',data=data)

def send_command(command,command_action,command_type):
    raw_command=get_recent_command()
 
    content=command[command_action]
    terse_units=content[0]
    single_command=content[1]
    for i,unit in enumerate(units_order):
        if terse_units[i]=='1':

            raw_command[unit][command_type]=single_command
    
    raw_command['time']=str(datetime.datetime.now())[:-7]
    data={'key':'19979476','content':str(raw_command)}
    requests.post(server+'/leader',data=data)
    with open('local_command.txt','w')as f:
        f.write(str(raw_command))



while True:
  try:
     time.sleep(1)
     with open('command_publish.txt','r')as f:
            command=f.read()
     if command=='over':
         pass
     else:
         command=eval(command)
         if 'affirm_alarm' in command:
             affirm_alarm()
             command_over()
         if 'send_command' in command:
             send_command(command,'send_command','command')
             command_over()
             
         if 'read_text' in command:
             text=command['read_text']
             os.system('ekho '+text)
             command_over()
         if  'publish_text' in command:
             send_command(command,'publish_text','text')
             command_over()
  except:
      time.sleep(3)
             
             

         
         
        
