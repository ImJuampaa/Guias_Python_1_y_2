import serial

class SerialCommunication:
    def __init__(self, port, baud_rate):
        self.serial_port = serial.Serial(port, baud_rate)
        self.initialize_communication()

    def initialize_communication(self):
        # Envia una instruccion al Arduino para que comience a enviar datos
        self.send_data("start")

    def read_data(self):
        return self.serial_port.readline().decode().strip()

    def send_data(self, data):
        self.serial_port.write(data.encode())

if __name__ == "__main__":
    serial_comm = SerialCommunication("/dev/ttyACM0", 19200)

    while True:
        arduino_data = serial_comm.read_data()
        print(f"Dato recibido desde el Arduino: {arduino_data}")