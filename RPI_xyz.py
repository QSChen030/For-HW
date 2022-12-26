#!/bin/python3
from sense_hat import SenseHat
import time
sense = SenseHat()

y = [255, 255, 0]
x = [0, 0, 0]
b = [0, 0, 255]
charx = 0
chary = 0

path=[
y,y,y,x,x,x,x,x,
x,x,y,x,x,x,x,x,
x,x,y,x,x,x,x,x,
x,x,y,y,y,y,y,x,
x,x,x,x,x,x,y,x,
x,x,x,x,x,x,y,x,
x,x,x,x,y,y,y,x,
x,x,x,x,y,x,x,x
]

sense.set_pixels(path)
sense.set_pixel(charx, chary, b)

while True:
   roll = sense.get_orientation()['roll']
   pitch = sense.get_orientation()['pitch']
   print("Roll: ", roll)
   print("Pitch: ", pitch)
   time.sleep(1)
   if 270 < pitch < 315 and charx < 7:
      charx += 1
   if 45 < pitch < 90 and charx > 0:
      charx -= 1
   if 270 <roll < 315 and roll < 7:
      chary += 1
   if 45 < roll < 90 and roll > 0:
      chary -= 1    
   sense.set_pixels(path)
   sense.set_pixel(charx, chary, b)
