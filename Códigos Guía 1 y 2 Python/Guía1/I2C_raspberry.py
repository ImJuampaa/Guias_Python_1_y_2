import time

# Direccion I2C del Arduino esclavo
arduino_address = 0x08

bus = smbus.SMBus(1)  # El numero 1 se refiere al bus I2C /dev/i2c-1

while True:
    try:
        # Solicita un byte de datos al Arduino esclavo
        data = bus.read_byte(arduino_address)
        print("Recibido:", data)
        time.sleep(1)
    except KeyboardInterrupt:
        break

bus.close()