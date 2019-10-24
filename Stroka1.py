
nachalo="ARconsole 2018.1.10"
arr=[]

with open('C:/Users/mkalyakin/10012018.csv') as file:
    print('open csv')
    for line in file:
        arr.append(line)
        print('append line')

for k in arr:

        sumstroka=''
        sumstroka=nachalo
        sumstroka = sumstroka+' C:\Autorevise\PILOT\\'+str(k)[:-1]+'\Routes'
        print (sumstroka)

    # for i in arr:
    #     sumstroka = sumstroka+' C:\Autorevise\PILOT\7701\Routes'
    # print (sumstroka)