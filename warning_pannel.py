#!/usr/bin/python3
# coding: utf-8
import pygame
import time
import os
import requests
units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','综合保障营','通信营','卫生队','阵管防卫连','机关楼','装备场区','共同训练场','营区大门岗','家属院门岗','油库']

def get_wire_status():
    with open('terse_affirm.txt','r')as f:
        status=eval(f.read())
    
    return status
def affirm_alarm():
     data={'key':'19979476','affirm':'all0'}
     requests.post(server+'/affirm',data=data)
     
def py_start(show):
    if show==0:
        pass
    else:
        #os.environ['SDL_VIDEO_CENTERED'] = '1'
        #os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(200,300)

        pygame.init()
        screen = pygame.display.set_mode((1920,1080), pygame.NOFRAME)
        background=pygame.image.load('warning_bg.png')

    
        f1=pygame.image.load('f1.png')
        f2=pygame.image.load('f2.png')
        f3=pygame.image.load('f3.png')
        f4=pygame.image.load('f4.png')
        f5=pygame.image.load('f5.png')
        f6=pygame.image.load('f6.png')
        f7=pygame.image.load('f7.png')
        f8=pygame.image.load('f8.png')
        f9=pygame.image.load('f9.png')
        f10=pygame.image.load('f10.png')
        f11=pygame.image.load('f11.png')
        f12=pygame.image.load('f12.png')
        f13=pygame.image.load('f13.png')
        f14=pygame.image.load('f14.png')
        f15=pygame.image.load('f15.png')
        f16=pygame.image.load('f16.png')
        f17=pygame.image.load('f17.png')
        f18=pygame.image.load('f18.png')
        f19=pygame.image.load('f19.png')
    
        f1_red=pygame.image.load('f1_red.png')
        f2_red=pygame.image.load('f2_red.png')
        f3_red=pygame.image.load('f3_red.png')
        f4_red=pygame.image.load('f4_red.png')
        f5_red=pygame.image.load('f5_red.png')
        f6_red=pygame.image.load('f6_red.png')
        f7_red=pygame.image.load('f7_red.png')
        f8_red=pygame.image.load('f8_red.png')
        f9_red=pygame.image.load('f9_red.png')
        f10_red=pygame.image.load('f10_red.png')
        f11_red=pygame.image.load('f11_red.png')
        f12_red=pygame.image.load('f12_red.png')
        f13_red=pygame.image.load('f13_red.png')
        f14_red=pygame.image.load('f14_red.png')
        f15_red=pygame.image.load('f15_red.png')
        f16_red=pygame.image.load('f16_red.png')
        f17_red=pygame.image.load('f17_red.png')
        f18_red=pygame.image.load('f18_red.png')
        f19_red=pygame.image.load('f19_red.png')
    
        show_units=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19]
        show_red_units=[f1_red,f2_red,f3_red,f4_red,f5_red,f6_red,f7_red,f8_red,f9_red,f10_red,f11_red,f12_red,
                    f13_red,f14_red,f15_red,f16_red,f17_red,f18_red,f19_red]
        light_on=pygame.image.load('警灯亮.png')
        light_off=pygame.image.load('警灯灭.png')
        affirm=pygame.image.load('确认警报按钮.png')
    
   
        screen.blit(background,(0,0))
        pygame.display.update()
    
        status=get_wire_status()
        show=sum(status)
    
        count=0
        while show:
            
            count+=1
            if count%5==0:
                screen.blit(light_off,(150,100))
            else:
                screen.blit(light_on,(150,100))
            
            pygame.display.update()
            
            start_x=600
            start_y=100
            
            for i,show_unit in enumerate(show_units):
                
                if i>=16:
                    screen.blit(show_unit,(start_x+(i-16)*300,start_y+100*5))
                elif i>=12:
                    screen.blit(show_unit,(start_x+(i-12)*300,start_y+100*4))
                elif i>=8:
                    screen.blit(show_unit,(start_x+(i-8)*300,start_y+100*3))
                elif i>=4:
                    screen.blit(show_unit,(start_x+(i-4)*300,start_y+100*2))
                else:
                    screen.blit(show_unit,(start_x+i*300,start_y+100))
            
            
            
            
            
            for i,show_red_unit in enumerate(show_red_units):
                
                if i>=16 and status[i]==1:
                    screen.blit(show_red_unit,(start_x+(i-16)*300,start_y+100*5))
                elif i>=12 and status[i]==1:
                    screen.blit(show_red_unit,(start_x+(i-12)*300,start_y+100*4))
                elif i>=8 and status[i]==1:
                    screen.blit(show_red_unit,(start_x+(i-8)*300,start_y+100*3))
                elif i>=4 and status[i]==1:
                    screen.blit(show_red_unit,(start_x+(i-4)*300,start_y+100*2))
                elif status[i]==1:
                    screen.blit(show_red_unit,(start_x+i*300,start_y+100))
            
            #pygame.display.update()
            
            screen.blit(affirm,(800,800))
            pygame.display.update()
            
            
            status=get_wire_status()
            show=sum(status)
            for event in pygame.event.get():#获得事件
                if event.type==pygame.MOUSEBUTTONDOWN and 800<=event.pos[0]<=800+700 and 800<=event.pos[1]<=800+95:
                    
                    command_publish={}
                    command_publish['affirm_alarm']='0'
                    with open('command_publish.txt','w')as f:
                        f.write(str(command_publish))
                    
   
                    status=[0 for i in range(0,19)]
                    
                    with open('terse_affirm.txt','w')as f:
                        f.write(str(status))
      
                    
   
                    with open('key_sound.txt','a')as f:
                        f.write('\n'+'affirm_alarm.mp3')
                    
                    show=0
                    
                  
             
        pygame.quit()
while True:
  try:
    status=get_wire_status()
    show=sum(status)
    py_start(show)
  except:
      time.sleep(2)
    
  