
with open('filename.txt') as fl:
    dat = fl.readlines()
    fl.close()
fdu_sn=list()
NODE=''
MAC1=list()
MAC2=list()
MAC=list()
start_point=0
curent_point = 0
for i in dat:
    #print(i)
    if i.find('NODE')==0 and NODE=='':
        NODE = i.split()[2]
    if i.find('NODE')>0 and i.find('sn:')>0:
        fdu_sn.append(i.split()[8])
        print(fdu_sn[-1])
for i in dat:

    if i.find('MAC1')>0 and i.find('MAC2')>0:
        start_point=curent_point+2
    if (start_point>0)and(start_point<=curent_point)and (curent_point<start_point+int(NODE)):
        MAC.append(i.split()[1:6])
        MAC.append(i.split()[6:])
        MAC1.append(i.split()[1:6])
        MAC2.append(i.split()[6:])
    curent_point+=1
print(start_point)
print('++++++++++++')
for i in sorted(MAC1, key=lambda M: int(M[0])):
    print(i)
print('++++++++++++')
for i in sorted(MAC2, key=lambda M: int(M[0])):
    print(i)
MAC3=MAC1+MAC2
print('++++++++++++')
for i in sorted(MAC3, key=lambda M: int(M[0])):
    print(i)
print('++++++++++++')
for i in sorted(MAC, key=lambda M: int(M[0])):
    print(i)
print(len(dat))
print(fdu_sn[5])
