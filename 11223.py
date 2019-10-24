import pandas as pd
import os
import numpy as np
import csv
for i in range (6):
    if i >=1:

        path = os.path.join(os.path.expanduser('~'),'Python_IP','ALL_IP_PY',str(i),'DNEVNIKI')
        print (path)

        path_save = os.path.join(os.path.expanduser('~'),'Python_IP','ALL_IP_PY','Saved')
        print (path)

        path_report = os.path.join(os.path.expanduser('~'),'Python_IP','ALL_IP_PY',str(i),'REPORTS')
        print (path_report)

        # Получаем список файлов в переменную files1
        files = os.listdir(path)
        print(files)

        # Фильтруем список по расширению и записываем его в массив S
        csv1 = filter(lambda x: x.endswith('.csv'), files)
        S1 = (list(csv1))

        # Получаем список файлов в переменную files1
        files1 = os.listdir(path_report)
        print(files1)

        # Фильтруем список по расширению и записываем его в массив S
        csv2 = filter(lambda x: x.endswith('.csv'), files1)
        S = (list(csv2))

        str1 = ''
        arr = []
        r = 0

        frame = pd.DataFrame()
        frame_report = pd.DataFrame()
        frame_dnev = pd.DataFrame()
        frame_rep = pd.DataFrame()

        list_ = []

        for file_ in S1:
            # with open(path+'/'+file_, 'r') as trainCsv:
            df1 = pd.read_csv(path+'/'+file_,index_col=None, sep=';', encoding='windows-1251')
            list_.append(df1)
            frame = pd.concat(list_)
        list_.clear()
        # print(frame)
        frame.drop(frame.columns[[0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]],axis=1, inplace=True)
        frame['Сумма'].replace(to_replace=',', value='.', inplace=True,regex=True, axis=1)
        frame['Сумма'] = frame['Сумма'].astype('float64')
        frame['Организация'] = frame['Организация'].apply(lambda x: x[:-27])
        frame['Организация'].replace(to_replace=' –', value='', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='–', value='', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace=' – ', value='', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='– ', value='', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Республики Северная Осетия-Алания-', value='УФПС Республики Северная Осетия-Алания', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='Республики Ко', value='Республики Коми', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='Красноярского кр', value='Красноярского края', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС г. Санкт-Петербурга и Ленинградской областити -', value='УФПС г. Санкт-Петербурга и Ленинградской областити', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Чеченской республи', value='УФПС Чеченской Республики', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Самарской области - ', value='УФПС Самарской области', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Республики Башкортостан -', value='УФПС Республики Башкортостан', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Республики Адыгея -', value='УФПС Республики Адыгея', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Пермского края -', value='УФПС Пермского края', inplace=True,regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Республики Бурят', value='УФПС Республики Бурятия',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Ненецкого автономного округа', value='УФПС Ненецкого Автономного Округа',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Мурманской облас', value='УФПС Мурманской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС г. Санкт-Петербурга и Ленинградской области -', value='УФПС Спб и Ленинградской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Архангельской области -', value='УФПС Архангельской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Забайкальского края ', value='УФПС Забайкальского края',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Ивановской области-', value='УФПС Ивановской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Липецкой облас', value='УФПС Липецкой области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Магаданской области-Филиал ФГУП «Почта-Росси', value='УФПС Магаданской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Саратовской облас', value='УФПС Саратовской области',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Ханты-Мансийского автономного округа', value='УФПС ХМАО',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС города Москвы', value='УФПС Москвы',
                                     inplace=True, regex=True, axis=1)
        frame['Организация'].replace(to_replace='УФПС Удмуртской Республики', value='УФПС Республики Удмуртия', inplace=True,regex=True, axis=1)

        frame['Сумма']=frame['Сумма'].abs()
        frame_dnev=frame.pivot_table(['Сумма'],['Организация'], aggfunc='sum', fill_value = 0)
        # frame_dnev.reset_index( inplace=True)
        print(frame)

        for file_ in S:
            # with open(path_report+'/'+file_, encoding='cp1251',mode='r') as trainCsv1:
            df = pd.read_csv(open(path_report+'/'+file_,'r'),index_col=None, sep=';')
            df['Организация'] = file_
            list_.append(df)
            frame_report = pd.concat(list_)
        frame_report.drop(frame_report.columns[[0, 1, 2, 4, 5, 6]], axis=1, inplace=True)
        frame_report['Сумма (во внешней системе)'].replace(to_replace=',', value='.', inplace=True,regex=True, axis=1)
        frame_report['Сумма (во внешней системе)'] = frame_report['Сумма (во внешней системе)'].astype('float64')
        frame_report['Организация'] = frame_report['Организация'].apply(lambda x: x[7:-4])
        frame_report['Сумма (во внешней системе)']=frame_report['Сумма (во внешней системе)'].abs()
        frame_rep=frame_report.pivot_table(['Сумма (во внешней системе)'],['Организация'], aggfunc='sum', fill_value = 0)
        # frame_rep.reset_index( inplace=True)


        OTVET1=[frame_dnev, frame_rep ]
        OTVET=pd.concat(OTVET1, axis=1)

        OTVET['Соотношение']=100*(OTVET['Сумма (во внешней системе)']/OTVET['Сумма'])
        print(OTVET)
        OTVET.to_csv(path_save+'/'+str(i)+'.csv',sep=';',encoding='windows-1251')