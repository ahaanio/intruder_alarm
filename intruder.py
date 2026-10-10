from machine import Pin, PWM, I2C
import utime
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq = 400000)
devices = i2c.scan()
i2c_address = devices[0]
lcd = I2cLcd(i2c, i2c_address, 2, 16)

pir = Pin(7, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(9))
servo = PWM(Pin(17))
servo.freq(50)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)
    
angle_values = [45, 90, 135, 90]

lcd.clear()
lcd.putstr("Starting...")
utime.sleep(5)

lcd.clear()
lcd.putstr("System Armed...")

trigger = False

counter = 0 

while True:
    for angle in angle_values:
        if not trigger:
            set_angle(angle)
            utime.sleep(0.5)
    
        if pir.value():
            if not trigger:
                counter = counter + 1
                lcd.clear()
                lcd.putstr("Intruder Alert!")
                lcd.move_to(0,1)
                lcd.putstr(f"Counter: {counter}")
                trigger = True

            buzzer.freq(600)       
            buzzer.duty_u16(32768)  
            utime.sleep(0.1)
                    
            buzzer.freq(900)       
            buzzer.duty_u16(32768) 
            utime.sleep(0.1)
            
            break
    
        else:
            if trigger:
                buzzer.duty_u16(0)
                lcd.clear()
                lcd.putstr("System Armed...")
                lcd.move_to(0,1)
                lcd.putstr(f"Counter: {counter}")
                trigger = False
            
    buzzer.duty_u16(0)
    utime.sleep(0.1)



