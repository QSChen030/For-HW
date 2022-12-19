from sense_hat import SenseHat
import time
sense = SenseHat()
while(True):
   temp = sense.get_temperature()
   print("溫度= ", temp)
   if (temp>28): #hot
       bg_color=(255,0,0)
   elif (temp<20): #cold
       bg_color=(0,0,255)
   else:  #fine
       bg_color=(0,255,0)
   t_str = str(round(temp,1)) 
   sense.show_message(t_str, 0.3,(255,255,255),bg_color)    
   time.sleep(0.5)
