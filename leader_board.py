#!/usr/bin/python3
# coding: utf-8

import datetime
from tkinter import *
from PIL import Image, ImageTk
import threading
import os
import time

time.sleep(2)

SUM_UNITS=19
    
def initialize_button_change():
    button_change=[] 
    for i in range(SUM_UNITS+4):
        button_change.append(0)
    with open('button_change.txt','w')as f:
        f.write(str(button_change))


def get_button_change():
    with open('button_change.txt','r')as f:
        button_change=eval(f.read())
    return button_change
def save_button_change(button_change):
    with open('button_change.txt','w')as f:
        f.write(str(button_change))

def image_change(p1,p2,butt,id_):
    button_change=get_button_change()
    if button_change[id_]==1:
        butt['image']=p1
        button_change[id_]=0
        save_button_change(button_change)
    elif button_change[id_]==0:
        butt['image']=p2
        button_change[id_]=1
        save_button_change(button_change)
    
    
def command_publish(command_type,command_content):
    command_publish={}
    command_publish[command_type]=command_content
    with open('command_publish.txt','r')as f:
        content=f.read()
    if content=='over':
        with open('command_publish.txt','w')as f:
            f.write(str(command_publish))
    else:
        print('too fast')
    
        
    



def open1():
    image_change(photo1,photo1_d,c1,0)
    
def open2():
    image_change(photo2,photo2_d,c2,1)

def open3():
    image_change(photo3,photo3_d,c3,2)

def open4():
    image_change(photo4,photo4_d,c4,3)

def send_all():
    button_change=get_button_change()

    command_aim=str(button_change[0])+str(button_change[1])+str(button_change[2])+str(button_change[3])
    
    command_select=''
    for s in button_change[4:]:
        command_select+=str(s)
        
    command_type='send_command'
    command_content=[command_select,command_aim]
    command_publish(command_type,command_content)
    key_sound('send_all.mp3')

    
def t1_s():
    image_change(photo6,photo6_s,t1,4)
def t2_s():
    image_change(photo6,photo6_s,t2,5)
def t3_s():
    image_change(photo6,photo6_s,t3,6)
def t4_s():
    image_change(photo6,photo6_s,t4,7)
def t5_s():
    image_change(photo6,photo6_s,t5,8)
def t6_s():
    image_change(photo6,photo6_s,t6,9)
def t7_s():
    image_change(photo6,photo6_s,t7,10)
def t8_s():
    image_change(photo6,photo6_s,t8,11)
def t9_s():
    image_change(photo6,photo6_s,t9,12)
def t10_s():
    image_change(photo6,photo6_s,t10,13)
def t11_s():
    image_change(photo6,photo6_s,t11,14)
def t12_s():
    image_change(photo6,photo6_s,t12,15)
def t13_s():
    image_change(photo6,photo6_s,t13,16)
def t14_s():
    image_change(photo6,photo6_s,t14,17)
def t15_s():
    image_change(photo6,photo6_s,t15,18)
def t16_s():
    image_change(photo6,photo6_s,t16,19)
def t17_s():
    image_change(photo6,photo6_s,t17,20)
def t18_s():
    image_change(photo6,photo6_s,t18,21)
def t19_s():
    image_change(photo6,photo6_s,t19,22)



def time_window():
    def get_time():
        year=str(datetime.datetime.now())[:4]
        month=str(datetime.datetime.now())[5:7]
        day=str(datetime.datetime.now())[8:10]
        hour=str(datetime.datetime.now())[11:13]
        minit=str(datetime.datetime.now())[14:16]
        return year,month,day,hour,minit
    
    def standard_time(year,month,day,hour,minit):
        if len(year)!=4 or int(year)<2019:
            return 'error'
        elif int(month) not in range(1,13):
            return 'error'
        elif int(day) not in range(1,32):
            return 'error'
        elif int(hour) not in range(0,25):
            return 'error'
        elif int(minit) not in range(0,61):
            return 'error'
        else:
            if len(month)<2:
                month='0'+month
            if len(day)<2:
                month='0'+month
            if len(hour)<2:
                month='0'+month
            if len(minit)<2:
                month='0'+month
            fixed_time=year+'-'+month+'-'+day+' '+hour+':'+minit+':'+'00'
            return fixed_time
            
        
            
    
    
    
    
    def quit_top():
        top.destroy()
    def save_time():
        fixed_time=standard_time(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get())
        if fixed_time=='error':
            key_sound('error_date.mp3')
        else:
            s=fixed_time.split(' ')
            os.system('sudo date --s='+s[0])
            os.system('sudo date --s='+s[1])
            key_sound('date_success.mp3')
  
  
  
    top = Toplevel()
    top.geometry('840x360')
    top.resizable(False, False) 
    top.overrideredirect(True)
    
    img= Label(top,image=photo_time_bg).place(x=0,y=0)
    
    
    windowWidth = 840   # 窗口宽
    windowHeight = 360   # 窗口高
    screenWidth, screenHeight = top.maxsize()      # 获得屏幕宽和高
    geometryParam = '%dx%d+%d+%d' % (
    windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
    top.geometry(geometryParam)           # 设置窗口大小及偏移坐标
    top.wm_attributes('-topmost',1)
    top.title("向指定单位发布命令")
    
    year,month,day,hour,minit=get_time()
    
    
    Label(top,text=year+' 年'+month+' 月'+day+' 日'+hour+' 时'+minit+' 分',bg='#C1C1C1',width=30,height=2,font=('Times','22')).place(x=200,y=35)
    
    
    
    
    interval=120
    e1 = StringVar()
    ent1 = Entry(top,textvariable=e1,width=4,bd=2,font=('Times','20'))
    e1.set(year)
    ent1.place(x=160,y=155) 
    
    e2 = StringVar()
    ent2 = Entry(top,textvariable=e2,width=3,bd=2,font=('Times','20'))
    e2.set(month)
    ent2.place(x=270,y=155) 
    
    e3 = StringVar()
    ent3 = Entry(top,textvariable=e3,width=3,bd=2,font=('Times','20'))
    e3.set(day)
    ent3.place(x=360,y=155) 
    
    e4 = StringVar()
    ent4 = Entry(top,textvariable=e4,width=3,bd=2,font=('Times','20'))
    e4.set(hour)
    ent4.place(x=455,y=155) 
    
    e5 = StringVar()
    ent5 = Entry(top,textvariable=e5,width=3,bd=2,font=('Times','20'))
    e5.set(minit)
    ent5.place(x=545,y=155) 

    Button(top,relief="ridge",image=photo_time_affirm,bd=5,command=save_time).place(x=100,y=210)
    Button(top,relief="ridge",image=photo_time_quit,bd=5,command=quit_top).place(x=450,y=210)
    



def text_window():
   
    def quit_top():
        top.destroy()
    def read_text():
        tick_time=4
        text=t1.get(0.0,END)
        if len(text)>50:
            text=text[:50]
            key_sound('over_text_50.mp3')
            tick_time+=4
        key_sound('read_text.mp3')
        time.sleep(tick_time)
        t2 = threading.Thread(target=read_tts_text,args=(text,))
        t2.start()
    def execut_ALARM_text():
        
        button_change=get_button_change()
        command_select=''
        for s in button_change[4:]:
            command_select+=str(s)
        text=t1.get(0.0,END)
        if len(text)>50:
            text=text[:50]
            key_sound('over_text_50.mp3')
        command_aim='ALARM'+text
        
        command_type='send_command'
        command_content=[command_select,command_aim]
        
        command_publish('publish_text',command_content)
        key_sound('execut_ALARM_text.mp3')

    def execut_BROAD_text():
        button_change=get_button_change()
        command_select=''
        for s in button_change[4:]:
            command_select+=str(s)
        text=t1.get(0.0,END)
        if len(text)>200:
            text=text[:200]
            key_sound('over_text_200.mp3')
        command_aim='BROAD'+'    '+text
        
        command_type='send_command'
        command_content=[command_select,command_aim]
        command_publish('publish_text',command_content)
        key_sound('execut_BROAD_text.mp3')
        
    top = Toplevel()
    top.geometry ('960x460')
    top.resizable(False, False) 
    top.overrideredirect(True)
    windowWidth =960   # 窗口宽
    windowHeight =460   # 窗口高
    screenWidth, screenHeight = top.maxsize()      # 获得屏幕宽和高
    geometryParam = '%dx%d+%d+%d' % (
    windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
    top.geometry(geometryParam)           # 设置窗口大小及偏移坐标
    top.wm_attributes('-topmost',1)
    top.title("向指定单位发布命令")
    
    img= Label(top,image=photo_text_bg).place(x=0,y=0)
   
    
    
    t1=Text(top,width=55,height=9,font=('song','19'))
    t1.place(x=36,y=37) 

    interval=226
    Button(top,relief="ridge",image=photo_text_read,bd=2,command=read_text,width=220,height=68).place(x=28,y=350)
    Button(top,relief="ridge",image=photo_text_sound_send,bd=2,command=execut_ALARM_text,width=220,height=68).place(x=28+1*interval,y=350)
    Button(top,relief="ridge",image=photo_text_words_send,bd=2,command=execut_BROAD_text,width=220,height=68).place(x=28+2*interval,y=350)
    Button(top,relief="ridge",image=photo_time_quit,bd=2,command=quit_top,width=220,height=68).place(x=28+3*interval,y=350)


def detail_window(sequence):
    def quit_top():
        top.destroy()
  
    units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','综合保障营','通信营','卫生队','阵管防卫连','机关楼','装备场区','共同训练场','营区大门岗','家属院门岗','油库']

    top = Toplevel()
    top.geometry ('1046x703')
    top.resizable(False, False) 
    top.overrideredirect(True)
    windowWidth =1046   # 窗口宽
    windowHeight =703   # 窗口高
    screenWidth, screenHeight = top.maxsize()      # 获得屏幕宽和高
    geometryParam = '%dx%d+%d+%d' % (
    windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
    top.geometry(geometryParam)           # 设置窗口大小及偏移坐标
    top.wm_attributes('-topmost',1)
    top.title("向指定单位发布命令")
    
    Label(top,image=photo_detail_bg).place(x=0,y=0) 
    
    Label(top,text=units_order[sequence],width=43,height=1,font=('song',24)).place(x=236,y=40) 
    
    text_type={'BROAD':'仅文字显示','ALARM':'语音朗读'}
    
    with open('local_command.txt','r')as f:
        local_command=eval(f.read())
        
        
    unit_text=local_command[units_order[sequence]]['text']
    unit_command=local_command[units_order[sequence]]['command']
    
    Label(top,text=text_type[unit_text[:5]],width=43,height=1,font=('song',24)).place(x=236,y=105)
    
    Label(top,text=unit_text[5:],width=80,height=7,font=('song',14),wraplength = 700,justify = 'left').place(x=245,y=173) 
    
    interval=80
    if unit_command[0]=='1':
        Label(top,image=photo_detail_red).place(x=100,y=440) 
    if unit_command[1]=='1':
        Label(top,image=photo_detail_yellow).place(x=100+interval*1,y=440) 
    if unit_command[2]=='1':
        Label(top,image=photo_detail_blue).place(x=100+interval*2,y=440) 
    if unit_command[3]=='1':
        Label(top,image=photo_detail_green).place(x=100+interval*3,y=440) 
    if unit_command=='0000':
        Label(top,image=photo_detail_no_alarm).place(x=100,y=440) 
    
    
    
    with open('situation.txt','r')as f:
        situation=eval(f.read())
    absence=situation['absence'][sequence]
    if absence=='1':
        Label(top,image=photo_detail_absence).place(x=480,y=450) 
    else:
        Label(top,image=photo_detail_presence).place(x=480,y=450) 
    
    alarm=situation['alarm'][units_order[sequence]]
    
    if int(alarm)>0:
        Label(top,image=photo_detail_alarm).place(x=750,y=450) 
    else:
        Label(top,image=photo_detail_safe).place(x=750,y=450) 
    
    Button(top,relief="ridge",image=photo_detail_quit,bd=0,command=quit_top).place(x=350,y=590)




def terse_alarm_show():
    with open('terse_alarm.txt','r')as f:
        terse_alarm=eval(f.read())
    interval=70
    for i in range(SUM_UNITS):
        Label(root,image=photo_set[i][0],width=58,height=257).place(x=134+i*interval,y=630)
   
            
def affirm_alarm():
    command_publish('affirm_alarm','0')
    key_sound('affirm_alarm.mp3')
    
def key_sound(mp3_name):
    with open('key_sound.txt','a')as f:
        f.write('\n'+mp3_name)

def read_tts_text(text):
    text=text.replace('连长','连掌').replace('营长','营掌').replace('旅长','旅掌')
    os.system('ekho '+text)


with open('terse_alarm.txt','r')as f:
    terse_alarm=f.read()
with open('terse_alarm_add.txt','w')as f:
    f.write(terse_alarm)




initialize_button_change()
root=Tk()
root.geometry('1920x1080')
root.title("高级用户终端")
#root.attributes('-fullscreen',True)
root.wm_attributes('-topmost',0)


photo=PhotoImage(file="高级用户终端背景.png")
img= Label(root,image=photo)
img.grid(row=0,column=0,rowspan=1000,columnspan=1000)

photo1=PhotoImage(file="红凸.png")
photo1_d=PhotoImage(file="红凹.png")
photo2=PhotoImage(file="黄凸.png")
photo2_d=PhotoImage(file="黄凹.png")
photo3=PhotoImage(file="蓝凸.png")
photo3_d=PhotoImage(file="蓝凹.png")
photo4=PhotoImage(file="绿凸.png")
photo4_d=PhotoImage(file="绿凹.png")
photo5=PhotoImage(file="发.png")
photo6=PhotoImage(file="勾选框空.png")
photo6_s=PhotoImage(file="勾选框选.png")
photo_time=PhotoImage(file="时间校准.png")
photo_text_command=PhotoImage(file="文本命令.png")
photo_affirm_alarm=PhotoImage(file="确认警报.png")
photo_detail=PhotoImage(file="详细情况按钮.png")
photo_u1_r=PhotoImage(file="发射一营-红.png")
photo_u1_w=PhotoImage(file="发射一营-白.png")
photo_u2_r=PhotoImage(file="发射二营-红.png")
photo_u2_w=PhotoImage(file="发射二营-白.png")
photo_u3_r=PhotoImage(file="发射三营-红.png")
photo_u3_w=PhotoImage(file="发射三营-白.png")
photo_u4_r=PhotoImage(file="发射四营-红.png")
photo_u4_w=PhotoImage(file="发射四营-白.png")
photo_u5_r=PhotoImage(file="发射五营-红.png")
photo_u5_w=PhotoImage(file="发射五营-白.png")
photo_u6_r=PhotoImage(file="发射六营-红.png")
photo_u6_w=PhotoImage(file="发射六营-白.png")
photo_u7_r=PhotoImage(file="技术一营-红.png")
photo_u7_w=PhotoImage(file="技术一营-白.png")
photo_u8_r=PhotoImage(file="技术二营-红.png")
photo_u8_w=PhotoImage(file="技术二营-白.png")
photo_u9_r=PhotoImage(file="作战保障营-红.png")
photo_u9_w=PhotoImage(file="作战保障营-白.png")
photo_u10_r=PhotoImage(file="综合保障营-红.png")
photo_u10_w=PhotoImage(file="综合保障营-白.png")
photo_u11_r=PhotoImage(file="通信营-红.png")
photo_u11_w=PhotoImage(file="通信营-白.png")
photo_u12_r=PhotoImage(file="卫生队-红.png")
photo_u12_w=PhotoImage(file="卫生队-白.png")
photo_u13_r=PhotoImage(file="阵管防卫连-红.png")
photo_u13_w=PhotoImage(file="阵地防卫连-白.png")
photo_u14_r=PhotoImage(file="机关楼-红.png")
photo_u14_w=PhotoImage(file="机关楼-白.png")
photo_u15_r=PhotoImage(file="装备场区-红.png")
photo_u15_w=PhotoImage(file="装备场区-白.png")
photo_u16_r=PhotoImage(file="共同训练场-红.png")
photo_u16_w=PhotoImage(file="共同训练场-白.png")
photo_u17_r=PhotoImage(file="营区大门岗-红.png")
photo_u17_w=PhotoImage(file="营区大门岗-白.png")
photo_u18_r=PhotoImage(file="家属院门岗-红.png")
photo_u18_w=PhotoImage(file="家属院门岗-白.png")
photo_u19_r=PhotoImage(file="油库-红.png")
photo_u19_w=PhotoImage(file="油库-白.png")


photo_set=([[photo_u1_w,photo_u1_r],[photo_u2_w,photo_u2_r],[photo_u3_w,photo_u3_r],[photo_u4_w,photo_u4_r],[photo_u5_w,photo_u6_r],[photo_u6_w,photo_u6_r],
            [photo_u7_w,photo_u7_r],[photo_u8_w,photo_u8_r],[photo_u9_w,photo_u9_r],[photo_u10_w,photo_u10_r],[photo_u11_w,photo_u11_r],[photo_u12_w,photo_u12_r],
            [photo_u13_w,photo_u13_r],[photo_u14_w,photo_u14_r],[photo_u15_w,photo_u15_r],[photo_u16_w,photo_u16_r],[photo_u17_w,photo_u17_r]
            ,[photo_u18_w,photo_u18_r],[photo_u19_w,photo_u19_r]])


photo_time_bg=PhotoImage(file="校时背景.png")
photo_time_affirm=PhotoImage(file="确认校准按钮.png")
photo_time_quit=PhotoImage(file="关闭窗口-文本输入.png")
photo_text_bg=PhotoImage(file="文本框输入背景.png")
photo_text_read=PhotoImage(file="本地试读按钮.png")
photo_text_sound_send=PhotoImage(file="语音发送按钮.png")
photo_text_words_send=PhotoImage(file="文本发送按钮.png")
photo_detail_bg=PhotoImage(file="详情背景.png")
photo_detail_red=PhotoImage(file="红灯.png")
photo_detail_yellow=PhotoImage(file="黄灯.png")
photo_detail_blue=PhotoImage(file="蓝灯.png")
photo_detail_green=PhotoImage(file="绿灯.png")
photo_detail_absence=PhotoImage(file="单位掉线.png")
photo_detail_presence=PhotoImage(file="单位在线.png")
photo_detail_alarm=PhotoImage(file="正在报警.png")
photo_detail_safe=PhotoImage(file="未报警.png")
photo_detail_quit=PhotoImage(file="关闭窗口长条按钮.png")
photo_detail_no_alarm=PhotoImage(file="四个灯不变.png")

c1=Button(root,relief="sunken", bd=0)
c1['image']=photo1
c1['command']=open1
c1.place(x=150,y=210)

c2=Button(root,relief="sunken", bd=0)
c2['image']=photo2
c2['command']=open2
c2.place(x=500,y=210)

c3=Button(root,relief="sunken", bd=0)
c3['image']=photo3
c3['command']=open3
c3.place(x=850,y=210)

c4=Button(root,relief="sunken", bd=0)
c4['image']=photo4
c4['command']=open4
c4.place(x=1200,y=210)

c5=Button(root, relief="ridge", bd=30)
c5['image']=photo5
c5['command']=send_all
c5.place(x=1540,y=175)

interval=70

t1=Button(root,relief="sunken",width=47,height=48, bd=0)
t1['image']=photo6
t1['command']=t1_s
t1.place(x=140,y=550)

t2=Button(root,relief="sunken",width=47,height=48, bd=0)
t2['image']=photo6
t2['command']=t2_s
t2.place(x=140+interval*1,y=550)

t3=Button(root,relief="sunken",width=47,height=48, bd=0)
t3['image']=photo6
t3['command']=t3_s
t3.place(x=140+interval*2,y=550)

t4=Button(root,relief="sunken",width=47,height=48, bd=0)
t4['image']=photo6
t4['command']=t4_s
t4.place(x=140+interval*3,y=550)

t5=Button(root,relief="sunken",width=47,height=48, bd=0)
t5['image']=photo6
t5['command']=t5_s
t5.place(x=140+interval*4,y=550)

t6=Button(root,relief="sunken",width=47,height=48, bd=0)
t6['image']=photo6
t6['command']=t6_s
t6.place(x=140+interval*5,y=550)

t7=Button(root,relief="sunken",width=47,height=48, bd=0)
t7['image']=photo6
t7['command']=t7_s
t7.place(x=140+interval*6,y=550)

t8=Button(root,relief="sunken",width=47,height=48, bd=0)
t8['image']=photo6
t8['command']=t8_s
t8.place(x=140+interval*7,y=550)

t9=Button(root,relief="sunken",width=47,height=48, bd=0)
t9['image']=photo6
t9['command']=t9_s
t9.place(x=140+interval*8,y=550)

t10=Button(root,relief="sunken",width=47,height=48, bd=0)
t10['image']=photo6
t10['command']=t10_s
t10.place(x=140+interval*9,y=550)

t11=Button(root,relief="sunken",width=47,height=48, bd=0)
t11['image']=photo6
t11['command']=t11_s
t11.place(x=140+interval*10,y=550)

t12=Button(root,relief="sunken",width=47,height=48, bd=0)
t12['image']=photo6
t12['command']=t12_s
t12.place(x=140+interval*11,y=550)

t13=Button(root,relief="sunken",width=47,height=48, bd=0)
t13['image']=photo6
t13['command']=t13_s
t13.place(x=140+interval*12,y=550)

t14=Button(root,relief="sunken",width=47,height=48, bd=0)
t14['image']=photo6
t14['command']=t14_s
t14.place(x=140+interval*13,y=550)

t15=Button(root,relief="sunken",width=47,height=48, bd=0)
t15['image']=photo6
t15['command']=t15_s
t15.place(x=140+interval*14,y=550)

t16=Button(root,relief="sunken",width=47,height=48, bd=0)
t16['image']=photo6
t16['command']=t16_s
t16.place(x=140+interval*15,y=550)

t17=Button(root,relief="sunken",width=47,height=48, bd=0)
t17['image']=photo6
t17['command']=t17_s
t17.place(x=140+interval*16,y=550)

t18=Button(root,relief="sunken",width=47,height=48, bd=0)
t18['image']=photo6
t18['command']=t18_s
t18.place(x=140+interval*17,y=550)

t19=Button(root,relief="sunken",width=47,height=48, bd=0)
t19['image']=photo6
t19['command']=t19_s
t19.place(x=140+interval*18,y=550)


Button(root,relief="ridge", bd=10,image=photo_time,command=time_window).place(x=1555,y=550)
Button(root,relief="ridge", bd=10,image=photo_text_command,command=text_window).place(x=1555,y=700)
Button(root,relief="ridge", bd=10,image=photo_affirm_alarm,command=affirm_alarm).place(x=1555,y=850)



interval=70
start_point=138
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(0)).place(x=start_point+interval*0,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(1)).place(x=start_point+interval*1,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(2)).place(x=start_point+interval*2,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(3)).place(x=start_point+interval*3,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(4)).place(x=start_point+interval*4,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(5)).place(x=start_point+interval*5,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(6)).place(x=start_point+interval*6,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(7)).place(x=start_point+interval*7,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(8)).place(x=start_point+interval*8,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(9)).place(x=start_point+interval*9,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(10)).place(x=start_point+interval*10,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(11)).place(x=start_point+interval*11,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(12)).place(x=start_point+interval*12,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(13)).place(x=start_point+interval*13,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(14)).place(x=start_point+interval*14,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(15)).place(x=start_point+interval*15,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(16)).place(x=start_point+interval*16,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(17)).place(x=start_point+interval*17,y=920)
Button(root,relief="ridge",image=photo_detail,bd=1,command=lambda:detail_window(18)).place(x=start_point+interval*18,y=920)

terse_alarm_show()

root.update_idletasks()
root.mainloop()
