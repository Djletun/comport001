from serial.tools import list_ports
import serial
import os

all_serial_ports = list_ports.comports()  # Outputs list of available serial ports
for i in range(len(all_serial_ports)):
    print(i,':',str(all_serial_ports[i]))

serial_port_nb = int(input('input Nb (0--):\n'))
serial_port_speed = 115200
#Serial takes two parameters: serial device and baudrate
if os.name=='nt':
    serial_port=str(all_serial_ports[serial_port_nb]).split()
if os.name=='posix':
    symbl='/'
print(serial_port[0])
ser = serial.Serial(serial_port[0], serial_port_speed)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
