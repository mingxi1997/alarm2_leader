#!/usr/bin/python3
# coding: utf-8

import requests
import time
server='http://192.168.1.4'
def get_situation():
    data={'key':'19979476'}
    res=requests.post(server+'/check',data=data)
    with open('situation.txt','w')as f:
        f.write(res.text)

    
def analysis(name):
    with open('situation.txt','r')as f:
        situation=eval(f.read())
    terse=[]
    for unit in units_order:
        a=situation[name][unit]
        if int(a)>0:
            t=1
        else:
            t=0
        terse.append(t)
    with open('terse_'+name+'.txt','w')as f:
        f.write(str(terse))

    
units_order=['发射一营','发射二营','发射三营','发射四营','发射五营','发射六营','技术一营','技术二营','作战保障营','综合保障营','通信营','卫生队','阵管防卫连','机关楼','装备场区','共同训练场','营区大门岗','家属院门岗','油库']

while True:
    try:
        time.sleep(2)
        get_situation()
        analysis('alarm')
        analysis('affirm')
    except:
        time.sleep(2)
     
         
    
     