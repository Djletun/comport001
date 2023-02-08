
with open('filename.txt') as fl:
    dat = fl.readlines()
    fl.close()
fdu_sn=list()
for i in dat:
    #print(i)
    if i.find('NODE')>0 and i.find('sn:')>0:
        fdu_sn.append(i.split()[8])
        print(fdu_sn[-1])
print(len(dat))
print(fdu_sn[5])
