from time import sleep, ticks_ms, ticks_add
import urequests
from secrets import api_key
from ujson import dumps
from led import Led
from button import Button
from machine import Pin, ADC, PWM


led_red = Led(21)
led_yellow = Led(22)
led_green = Led(19)
button_left = Button(23)
button_right = Button(18)

Qualidade=["boa","moderada","não saudável para grupos sensíveis","Pouco saudável","Muito insalubre","Perigoso"]
var=["pm25","o3","so2","co"]
varbutton=1
Gases=['Ozono', 'Deóxido de enxofre','monóxido de carbono']
unidades=["μg/m3","μg/m3","ppm"]

def x(varb):
  a=r["data"]["iaqi"][var[varbutton]]["v"]
  if varb==0: #aqi
    return int(a/50)
  elif varb==1:#limites tabelados para o3
    if a<160:
      return int(a/80)
    elif 160<=a<200:
      return 2
    elif 200<=a<800:
      return 3
    elif 800<=a<1000:
      return 4 
    else:
      return 5
  elif varb==2: #limites tabelados para so2
    if a<80:
      return 0
    elif 80<=a<366:
      return 1
    elif 366<=a<800:
      return 2
    elif 800<=a<1600:
      return 3
    elif 1600<=a<2100:
      return 4
    else:
      return 5
  elif varb==3: #limites tabelados para co
    if a<=15:
      return int(a/5)
    elif 15<=a<30:  
      return 3
    elif 30<=a<40:
      return 4
    else:
      return 5




def ledproc(x,y):
  a=r["data"]["iaqi"][var[varbutton]]["v"]
  print(x)
  led_yellow.off()
  led_green.off()
  led_red.off()
  if (x==0 or x==1 or x==3):
    led_green.on()
 
  if (x==1 or x==2 or x==4):
    led_yellow.on()
  
  if x>=3:
    led_red.on()
  

  if y==0:
    print("A qualidade do ar em {0} é {1}, com um índice de qualidade {2}" .format(location, Qualidade[x],a))
  else:
    print("A quantidade de {0} no ar em {1} é {2}, com valor {3} {4}" .format(Gases[y-1],location, Qualidade[x],a,unidades[y-1]))

  



while True:
    
  location = "Shangai"
  url = "https://api.waqi.info/feed/{0}/?token={1}" \
    .format(location, api_key)
  r = urequests.get(url).json()

  
  rep=varbutton
  while (varbutton==rep):
    if button_left.state():
      sleep(0.5)
      if varbutton == 3:
        print("Não há mais analises")
      else:
        varbutton+=1
        b=x(varbutton)
        ledproc(b,varbutton)
      

    elif button_right.state():
      sleep(0.5)
      if varbutton==0:
        print("Não há mais análises")
      else:
        varbutton-=1
        b=x(varbutton)
        ledproc(b,varbutton)
    else: 
      continue