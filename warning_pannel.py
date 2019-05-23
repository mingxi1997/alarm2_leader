#!/usr/bin/python3
# coding: utf-8
import pygame
import time

units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','阵管防卫连','营区大门岗','家属院门岗','油库','机关楼','装备场区','共同训练场']

def get_wire_status():
    with open('terse_affirm.txt','r')as f:
        status=eval(f.read())
    return status

BLUE=(16,79,186)
YELLOW=(255,255,0)


def py_start():
    pygame.init()
    pygame.display.set_caption('注意警报！！！')
    screen=pygame.display.set_mode((480,320),0,24)
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
    
    show_units=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16]
    
    under_show=pygame.image.load('sdjb.png')
       
    show=True

    screen.blit(background,(0,0))
    pygame.display.update()
    while show:
        
        screen.blit(under_show,(60,200))
        pygame.display.update()
        
        status=get_wire_status()
        show=sum(status)

        
            
        while show:   
            circle=[]
            for i,s in enumerate(status):
                if status[i]==1:
                    circle.append(show_units[i])
            for c in circle:
                screen.blit(c,(80,50))
                pygame.display.update()
                time.sleep(3)
            status=get_wire_status()
            show=sum(status)
         
        
        
        
    pygame.quit()

while True:
    status=get_wire_status()
    show=sum(status)
   
    if show>=1:
        
        py_start()
    else:
        time.sleep(3)