from serial.tools import list_ports
import serial
import os
import time

def serial_port_cmd(ser, input_cmd):
    ser.write(bytes(input_cmd, 'utf-8'))
    ser.flush()
    sleep_time = 0.05
    out = list()
    while ser.inWaiting() > 0:  # self.serial.readable() and
        s = ''
        s = str(ser.readline())
        time.sleep(sleep_time)
        s = s.replace('b\'', '')
        s = s.replace('\\r\\n\'', '')
        s = s.replace('\'', '')
        out.append(s)
    return out


all_serial_ports = list_ports.comports()  # Outputs list of available serial ports
for i in range(len(all_serial_ports)):
    print(i, ':', str(all_serial_ports[i]))

# serial_port_nb = int(input('input Nb (0--):\n'))
serial_port_nb = 2
serial_port_speed = 115200
# Serial takes two parameters: serial device and baudrate
if os.name == 'nt':
    serial_port = str(all_serial_ports[serial_port_nb]).split()
if os.name == 'posix':
    symbl = '/'

ser = serial.Serial(serial_port[0], serial_port_speed, bytesize=8, parity='N', stopbits=1, timeout=1, write_timeout=1)
ser.set_buffer_size(rx_size=12800, tx_size=12800)

input_cmd = '\r\n'
k1 = serial_port_cmd(ser, input_cmd)[:]
for i in k1:
    print(i)
#CONC_NB = output_list[2].split()[1]
#last_line = str(output_list[2])
input_cmd = 's::line::status' + '\r\n'
k2 = serial_port_cmd(ser, input_cmd)[:]
for i in k2:
    print(i)

input_cmd = 's_node_debug_showSigproCrcCounters \"LOW\",1,' + str(len(k2) - 17) + '\r\n'
k3 = serial_port_cmd(ser, input_cmd)[:]
for i in k3:
    print(i)

with open('filename.txt', 'w') as fl:
    for i in k1:
        fl.write(i)
        fl.write('\n')
    for i in k2:
        fl.write(i)
        fl.write('\n')
    fl.writelines(k2)
    for i in k3:
        fl.write(i)
        fl.write('\n')
#    fl.writelines(k1)
#    fl.writelines(k2)
    fl.writelines(k3)
    fl.close()
print(len(k1))
print(len(k2))
print(len(k3))