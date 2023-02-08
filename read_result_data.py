
with open('filename.txt') as fl:
    dat = fl.readlines()
    fl.close()
for i in dat:
    print(i)
print(len(dat))