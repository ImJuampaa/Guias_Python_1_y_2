import smbus
import time

class ArduinoI2C:
    def __init__(self, address):
        self.bus = smbus.SMBus(1)  # El número 1 se refiere al bus I2C /dev/i2c-1
        self.address = address

    def read_random_number(self):
        try:
            # Solicita un byte de datos al Arduino esclavo
            data = self.bus.read_byte(self.address)
            return data
        except IOError:
            print("Error de comunicación I2C")
            return None

if __name__ == "__main__":
    arduino_address = 0x08  # Dirección I2C del Arduino esclavo
    arduino = ArduinoI2C(arduino_address)

    try:
        while True:
            data = arduino.read_random_number()
            if data is not None:
                print("Recibido:", data)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        arduino.bus.close()