import os
import xlwt
from datetime import datetime
from datetime import date
from time import time


# Вытаскиваем сегодняшнюю дату
GETDATE = str(date.today())
GETTIME = int(time())
# Создаем новый отчет в excel
wb = xlwt.Workbook()
print('Создается новый ежедневный отчет')

# Создаем лист в отчете
ws = wb.add_sheet('Отчет')
print('Создается лист в excel-файле')

#добавляем таймер
tic = time()

#Записываем данные в 1 строку Excel,
#  методу write передаем номер строки(первое число) и номер столбца (второе число), а также то, что нужно вписать в ячейку

ws.write(0, 3, 'Название')

#Записываем шапку во вторую строку(индксация в Python начинается с 0, поэтому для записи во 2 строку пишем 1)
ws.write(1, 1, 'Сверок всего')
ws.write(1, 2, 'Расхождений')
ws.write(1, 3, 'Ненулевых совпадений')
print('Добавляется шапка отчета')

# Каталог из которого будем брать файлы
directory = 'D:/Работа/ДЛЯ ОПЦ И МПК/18.02 OPC'
reportdirectory = 'D:/Работа/ДЛЯ ОПЦ И МПК/18.02 OPC/'

#Указываем, если нам нужна определенная система
extsys='МПК'

# Получаем список файлов в переменную files1
files1 = os.listdir(directory)

# Фильтруем список по расширению и записываем его в массив S
csv = filter(lambda x: x.endswith('.csv'), files1)
S = (list(csv))

str1 = ''
arr = []
r = 0

#Для каждого файла из списка: открываем файл, пропускаем первую строку(шапку) и
# добавляем строки в массив с разделителем ';', также добавляем к строке название УФПС с помощью среза с названия файла
for x in S:
    with open(directory+'/{}'.format(x)) as file:
        print('Открываем   ' + x)
        line = file.readline()
        for line in file:
            if extsys in line:
                str1 = x[7:-4] + ';' + line
                arr.append(str1.split(';'))
        print('Добавляем строки из '+x)

#Смещение массива
for line in (arr):
    if len(line) == 10:
        line[2] = line[2][1:] + ';' + line[3][:-1]
        line[3] = line[4]
        line[4] = line[5]
        line[5] = line[6]
        line[6] = line[7]
        line[7] = line[8]
        line[8] = line[9]
        print('delete "')
        # print(line)
    if len(line) == 11:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4][:-1]
        line[3] = line[5]
        line[4] = line[6]
        line[5] = line[7]
        line[6] = line[8]
        line[7] = line[9]
        line[8] = line[10]
        print('delete "')
    if len(line) == 12:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5][:-1]
        line[3] = line[6]
        line[4] = line[7]
        line[5] = line[8]
        line[6] = line[9]
        line[7] = line[10]
        line[8] = line[11]
        print('delete "')
    if len(line) == 13:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6][:-1]
        line[3] = line[7]
        line[4] = line[8]
        line[5] = line[9]
        line[6] = line[10]
        line[7] = line[11]
        line[8] = line[12]
        print('delete "')
    if len(line) == 14:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6] + ';' + line[7][:-1]
        line[3] = line[8]
        line[4] = line[9]
        line[5] = line[10]
        line[6] = line[11]
        line[7] = line[12]
        line[8] = line[13]
        print('delete "')
    if len(line) == 15:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6] + ';' + line[7] + ';' + line[8][:-1]
        line[3] = line[9]
        line[4] = line[10]
        line[5] = line[11]
        line[6] = line[12]
        line[7] = line[13]
        line[8] = line[14]
        print('delete "')
    if len(line) == 16:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6] + ';' + line[7] + ';' + line[8] + ';' + line[9][:-1]
        line[3] = line[10]
        line[4] = line[11]
        line[5] = line[12]
        line[6] = line[13]
        line[7] = line[14]
        line[8] = line[15]
        print('delete "')
    if len(line) == 17:
        # print(line)
        line[2] = line[2][1:] + ';' + line[3] + ';' + line[4] + ';' + line[5] + ';' + line[6] + ';' + line[7] + ';' + line[8] + ';' + line[9] + ';' + line[10][:-1]
        line[3] = line[11]
        line[4] = line[12]
        line[5] = line[13]
        line[6] = line[14]
        line[7] = line[15]
        line[8] = line[16]
        print('delete "')

#Вводим переменные для результатов
stroka = ''
syst = ''
alll = 0
covpsnot0 = 0
diff = 0

UFPS = set()
for j in range(len(arr)):
    set(arr[j][0])
    UFPS.add(arr[j][0])
UFPS_LIST = list(UFPS)
print(UFPS_LIST)

t = 0
ROW_COUNT = 2
UFPS_COUNT = 0
for n in UFPS_LIST:
    #обнуляем счетчики
    alll = 0
    covpsnot0 = 0
    diff = 0
#для каждого УФПС из всех полученных УФПС считаем показатели

    for i in range(len(arr)):
        # if arr[i][2] == '2.12.':
            if arr[i][0] == UFPS_LIST[UFPS_COUNT]:
            #всего сверок
                alll += 1
                #ненулевых совпадений
                if arr[i][6] == '0' and (arr[i][4] != 0 and arr[i][5] != '0'):
                    covpsnot0 += 1
                #расхождений
                if arr[i][6] != '0':
                    diff += 1
    if alll != 0:
        # ws.write(ROW_COUNT, 1, date)
        ws.write(ROW_COUNT, 0, n)
        ws.write(ROW_COUNT, 1, alll)
        ws.write(ROW_COUNT, 2, diff)
        ws.write(ROW_COUNT, 3, covpsnot0)

    ROW_COUNT += 1
    print('iteration', ROW_COUNT)
    t += 1
    print(t)
    UFPS_COUNT += 1
ws.write(0, 0, extsys)
t = 0
toc=time()
print(toc - tic)


wb.save(reportdirectory+'Report-'+GETDATE+'-'+str(GETTIME)+'.xls')