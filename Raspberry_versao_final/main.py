from machine import I2C, Pin, ADC
from time import sleep
from pico_i2c_lcd import I2cLcd


i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


ldr_pin = ADC(Pin(26))

while True:
    ldr_value = ldr_pin.read_u16()  
    
    lcd.clear()
    lcd.putstr("Valor do LDR(ohm): {}".format(ldr_value))

    sleep(1)
