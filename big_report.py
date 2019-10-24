import re
import os
import xlrd
import xlwt
from datetime import datetime
from datetime import date
import zipfile

# Вытаскиваем сегодняшнюю дату
GETDATE = str(date.today())
# Создаем новый отчет в excel
wb = xlwt.Workbook()
print('Создается новый ежедневный отчет')
# Создаем лист в отчете
ws = wb.add_sheet('Отчет')
ws2 = wb.add_sheet('Отчет2')
print('Создается лист в excel-файле')

ws.write(0, 0, 'Название')
ws.write(0, 1, 'Регион')
ws.write(0, 2, 'Внешняя система')
ws.write(0, 3, 'Строка')
ws.write(0, 4, 'Всего сверок')
ws.write(0, 5, 'Совпадений, когда везде нули')
ws.write(0, 6, 'Совпадений, когда есть значения')
ws.write(0, 7, 'Расхождений')
ws.write(0, 8, '0 только в дневнике')
ws.write(0, 9, '0 только в ИС')
ws.write(0, 10, 'расхождения ненулевые')
print('Добавляется шапка отчета')

# Каталог из которого будем брать файлы для ежедневных отчетов
directory = 'C:/Users/Mkalyakin/Desktop/Отчёте 28-30/УФПС'

# Получаем список файлов в переменную files
files1 = os.listdir(directory)

# Фильтруем список по расширению
csv = filter(lambda x: x.endswith('.csv'), files1)
S = (list(csv))
str1 = ''
arr = []
r = 0
for x in S:
    with open('C:/Users/Mkalyakin/Desktop/Отчёте 28-30/УФПС/{}'.format(x)) as file:
        line = file.readline()
        for line in file:
            str1 = x[7:-8] + ';' + line
            arr.append(str1.split(';'))

for r in range(len(arr)):
    if '"' in arr[r][2]:
        if len(arr[r]) == 10:
            arr[r][2] = arr[r][2][1:] + ';' + arr[r][3][:-1]
            arr[r][3] = arr[r][4]
            arr[r][4] = arr[r][5]
            arr[r][5] = arr[r][6]
            arr[r][6] = arr[r][7]
            arr[r][7] = arr[r][8]
            arr[r][8] = arr[r][9]
        if len(arr[r]) == 11:
            arr[r][2] = arr[r][2][1:] + ';' + arr[r][3] + ';' + arr[r][4][:-1]
            arr[r][3] = arr[r][5]
            arr[r][4] = arr[r][6]
            arr[r][5] = arr[r][7]
            arr[r][6] = arr[r][8]
            arr[r][7] = arr[r][9]
            arr[r][8] = arr[r][10]
        if len(arr[r]) == 12:
            arr[r][2] = arr[r][2][1:] + ';' + arr[r][3] + ';' + arr[r][4] + arr [r][5] [:-1]
            arr[r][3] = arr[r][6]
            arr[r][4] = arr[r][7]
            arr[r][5] = arr[r][8]
            arr[r][6] = arr[r][9]
            arr[r][7] = arr[r][10]
            arr[r][8] = arr[r][11]

stroka = ''
syst = ''
alll = 0
covps0 = 0
covpsnot0 = 0
diff = 0
diffvdn = 0
diffvsys = 0
notnuldiff = 0


arrset = set()
for j in range(len(arr)):
    set(arr[j][2])
    arrset.add(arr[j][2])
l = list(arrset)
print(l)


arrsett = set()
for j in range(len(arr)):
    set(arr[j][0])
    arrsett.add(arr[j][0])
jopa = list(arrsett)
print(jopa)

t = 0
tt = 1
ttt=0
for hui in jopa:
    for j in l:
        for i in range(len(arr)):
            stroka = j
            if arr[i][2] == l[t]:
                alll += 1
                if arr[i][4] == '0' and arr[i][5] == '0':
                    covps0 += 1
                if arr[i][6] == '0' and (arr[i][4] != 0 or arr[i][5] != '0'):
                    covpsnot0 += 1
                if arr[i][6] != '0':
                    diff += 1
                if arr[i][6] != '0' and arr[i][5] == '0':
                    diffvdn += 1
                if arr[i][6] != '0' and arr[i][4] == '0':
                    diffvsys += 1
                if arr[i][6] != '0' and (arr[i][4] != 0 or arr[i][5]!='0'):
                    notnuldiff += 1
                syst = arr[i][3]
        ws.write(tt, 3, stroka)
        ws.write(tt, 0, hui)
        ws.write(tt, 2, syst)
        ws.write(tt, 4, alll)
        ws.write(tt, 5, covps0)
        ws.write(tt, 6, covpsnot0)
        ws.write(tt, 7, diff)
        ws.write(tt, 8, diffvdn)
        ws.write(tt, 9, diffvsys)
        ws.write(tt, 10, notnuldiff)
        tt += 1
        t += 1
        alll = 0
        covps0 = 0
        covpsnot0 = 0
        diff = 0
        diffvdn = 0
        diffvsys = 0
        notnuldiff = 0

    t = 0
    print(tt)

wb.save('C:/Users/Mkalyakin/Desktop/Отчёте 28-30/УФПС//Big-Report-'+GETDATE+'.xls')