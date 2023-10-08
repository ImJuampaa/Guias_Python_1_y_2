import smbus
import serial
import time
class ArduinoI2C:
    def __init__(self, address):
        self.bus = smbus.SMBus(1)  
        self.address = address
    def request_data(self):
        try:
            self.bus.write_byte(self.address, 1)  
            time.sleep(0.1) 
            data = self.ser.readline().decode().strip()
            return data
        except IOError:
            print("Error de comunicacion I2C")
            return None
class SensorTemperatura:
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)
    def read_temperature(self):
        try:
            temperatura = self.ser.readline().decode().strip()
            return temperatura
        except Exception as e:
            print("Error al leer la temperatura:", str(e))
            return None

class TemperaturaLogger:
    def __init__(self, filename):
        self.filename = filename
        self.datos = []
        self.tiempo_inicial = time.time()
	self.tiempo_guardar_promedio = 5 * 60  

    def log_temperatura(self, temperatura_str):
        tiempo_actual = time.time()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tiempo_actual))
        print(f"{timestamp} - T: {temperatura_str}")
        temperatura_num = float(temperatura_str.split()[1]) 
        self.datos.append((tiempo_actual, temperatura_num))
        if tiempo_actual - self.tiempo_inicial >= self.tiempo_guardar_promedio:
            self.calcular_y_guardar_promedio()
            self.tiempo_inicial = tiempo_actual
    def calcular_y_guardar_promedio(self):
        if not self.datos:
            return
        promedio = sum(temperatura for _, temperatura in self.datos) / len(self.datos)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.datos[-1][0]))
        with open(self.filename, "a") as archivo:
            archivo.write(f"Promedio: {promedio:.2f}°C - Timestamp: {timestamp}\n")
        print(f'Promedio: {promedio:.2f}°C - Timestamp: {timestamp}')
        self.datos = []
if __name__ == "__main__":
    arduino_address = 0x08  
    arduino = ArduinoI2C(arduino_address)
    sensor = SensorTemperatura('/dev/ttyACM0')  
    logger = TemperaturaLogger("temperatura_promedio.txt")
    try:
        while True:
            temperatura = sensor.read_temperature()
            if temperatura is not None:
                logger.log_temperatura(temperatura)
            time.sleep(30)  
    except KeyboardInterrupt:
        pass
    finally:
        sensor.ser.close()