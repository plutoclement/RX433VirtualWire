import time

import pigpio
#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
R�ception d'un message par le Raspberry Pi,
re�u � 433 MHz par un r�cepteur
reli� � la pin GPIO 11
N�cessite la pr�sence du fichier vw.py dans le 
m�me r�pertoire.
http://www.raspberrypi.org/forums/viewtopic.php?t=84596&p=598087

'''

import vw

RX=11

BPS=2000

pi = pigpio.pi() 

rx = vw.rx(pi, RX, BPS) 

start = time.time()

print("En attente de la reception des donnees")

while (time.time()-start) < 100:

   while rx.ready():
      print("".join(chr (c) for c in rx.get()))

rx.cancel()

pi.stop()