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

err=0

input_cmd = '\r\n'
k1 = serial_port_cmd(ser, input_cmd)[:]
for i in k1:
    print(i)
# CONC_NB = output_list[2].split()[1]
# last_line = str(output_list[2])
input_cmd = 's::line::status' + '\r\n'
k2 = serial_port_cmd(ser, input_cmd)[:]
NODE = ''
fdu_sn = list()
for i in k2:
    print(i)
    if i.find('NODE') == 0 and NODE == '':
        NODE = i.split()[2]
    if i.find('NODE') > 0 and i.find('sn:') > 0:
        fdu_sn.append(list(i.split()[8]))
print("NODE=", NODE)
input_cmd = 's_node_debug_showSigproCrcCounters \"LOW\",1,' + NODE + '\r\n'
k3 = serial_port_cmd(ser, input_cmd)[:]
MAC = list()
start_point = 0
curent_point = 0
for i in k3:
    if i.find('No node on line segment')>0:
        err=10
        break
    if i.find('MAC1') > 0 and i.find('MAC2') > 0:
        start_point = curent_point + 2
    if (start_point > 0) and (start_point <= curent_point) and (curent_point < start_point + int(NODE)):
        MAC.append(i.split()[1:6])
        MAC.append(i.split()[6:])
    curent_point += 1
    print(i)
print('++++++++++++')
MAC_s=sorted(MAC, key=lambda M: int(M[0]))
for i in MAC_s:
    print(i)

for i in range(len(fdu_sn)):
    fdu_sn[i].append(MAC_s[2*i])
    fdu_sn[i].append(MAC_s[2*i+1])
print('++++++++++++++++++++')
for i in fdu_sn:
    print(*i)
with open('filename2.txt', 'w') as fl:
    for i in sorted(MAC, key=lambda M: int(M[0])):
        fl.write(' '.join(i))
        fl.write('\n')
    # fl.writelines(k3)
    fl.close()

