from machine import Pin, PWM, I2C
import utime
from pico_i2c_lcd import I2cLcd
import neopixel

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq = 400000)
devices = i2c.scan()
i2c_address = devices[0]
lcd = I2cLcd(i2c, i2c_address, 2, 16)

num_leds = 8
np_pin = Pin(18, Pin.OUT)
np = neopixel.NeoPixel(np_pin, num_leds)

pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(15))
buzzer.duty_u16(0) ## Fixed buzzer logic

def set_color(r, g, b):
    for i in range(num_leds):
        np[i] = (r, g, b)
    np.write()
    
lcd.clear()
lcd.putstr("Starting...")
set_color(0, 0, 0)
utime.sleep(5)

lcd.clear()
lcd.putstr("System Armed...")
set_color(0, 40, 0)

trigger = False

counter = 0 

while True:
    if pir.value():
        if not trigger:
            counter = counter + 1
            lcd.clear()
            lcd.putstr("Intruder Alert!")
            lcd.move_to(0,1)
            lcd.putstr(f"Counter: {counter}")
            trigger = True
            buzzer = PWM(Pin(15))
            
        for i in range(4):
            np[i] = (255, 0, 0)
            np[i+4] = (0, 0, 255)
        np.write()

        buzzer.freq(600)       
        buzzer.duty_u16(32768)  
        utime.sleep(0.1)
        
        for i in range(4):
            np[i] = (0, 0, 255)
            np[i+4] = (255, 0, 0)
        np.write()
                    
        buzzer.freq(900)       
        buzzer.duty_u16(32768) 
        utime.sleep(0.1)
    
    else:
        if trigger:
            buzzer.duty_u16(0)
            lcd.clear()
            lcd.putstr("System Armed...")
            set_color(0, 40, 0)
            lcd.move_to(0,1)
            lcd.putstr(f"Counter: {counter}")
            trigger = False
    
    utime.sleep(0.1)



