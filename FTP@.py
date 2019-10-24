from ftplib import FTP
import re
import datetime
import os, sys, os.path
now = datetime.datetime.now()
dir = 'C:/Users/Mkalyakin/Documents/Python_IP/'
dates=[]
for i in range(31):
    if 1<=i<10:
        dates.append('17100'+str(i))
    if i>=10:
        dates.append('1710'+str(i))
print (dates)
arr=set()
KPP_LIST=[]
with open('C:/Users/Mkalyakin/Documents/KPP_ALL.csv') as file:
    print(' Загружаем список КПП')
    for line in file:
       KPP_LIST.append(line[:-1])
for kpp in KPP_LIST:
    for date in dates:
        with FTP('ftp.caits.ru', 'InformPunkt', 'Sw@44asz') as ftp:
            filenames=[]
            arr=[]
            ftp.cwd('/1c_f130raw/'+kpp+'/')
            filenames = ftp.nlst()
            for file in filenames:
                # print(file)
                if file.endswith(date+'_2.zip'):
                    arr.append(file)
            for string in arr:
                with open(dir + string, 'wb') as f:
                    ftp.retrbinary('RETR ' + string, f.write)

