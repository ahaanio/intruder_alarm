This raspberry pi pico circuit contains a WS2812 led strip, a HC-SR501 PIR motion sensor, an I2C LCD1602 screen, and a passive buzzer. When the system is 
idle, the led strip is green, and the lcd scren displays "System Armed..." and displays a counter of how many times the alarm has been tripped. When the PIR 
motion sensor detects someone, the passive buzzer lets out a police siren noise, the led flashes red and blue, and the lcd updates the screen to say "Intruder 
Alert!" and updates the counter. 

Notes: Make sure to use a transistor for the passive buzzer! I used it without a transistor the first run through, and the buzzer made a faint whirring sound 
while the circuit was on. The transistor I used was a S8050. For this code to work, you must follow the wiring. The lcd screen's GND is connected to the negative 
rail of the breadboard, which connects to any GND on the microcontroller. The VCC pin goes to the postive rail of the breadboard, which is connected to the VBUS pin 
of the pico. The SDA is connected to GP0, and SCL is connected to GP1. Then, the buzzer's postive leg is connected to the other postive rail, which connects to the 
pico's 3v3 OUT. When connecting the transistor, make sure the flat side with the number printed on it is facing you when wiring for this project. The right most leg 
is connected to the negative leg of the buzzer. The middle leg is connected to a resistor, which then connects to GP15. The left most leg is connected to any GND on 
controller. For the PIR motion sensor, the GND is connected to the negative rail, the OUT is connected to GP16, and the VCC is connected to the VBUS via the 
postive rail. Finally, the led light strip had the GND connected to the negative rail, the DIn to GP18, and the 5V connected to the postive rail with VBUS. I 
checked for short circuits using a multimeter, just to make sure nothing breaks. Have fun using your new security alarm!
