import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

while True:
    s= ser.readline()
    s= s.strip()
    print (s.decode("utf-8"))