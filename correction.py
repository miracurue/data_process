import pandas as pd
import numpy as np
from datetime import datetime
import re




def lower_strip(df, df_full: bool):
    ''' 
    Функция приводит все данные к нижнему регистру и убирает пробелы и запятые по краям.
    В функцию можно передавать как целый датафрейм, так и одну колонку.

    При df_full = True функция работает с df как с датафреймом
    При df_full = False функция работает с df как с колонкой
    
    При работе с датафреймом если тип данных в столбце отличен от str, то функция пропустит этот столбец
    Перед работой все пропущенные значения заполняются пустыми строками, а при возврате пустые строки заменяются на np.nan
    
    '''
    if df_full:
        for column in [col for col in df.columns.to_list() if df[col].dtype == 'object']:
            df[column] = df[column].fillna('')
            df[column] = df[column].str.lower().str.strip(' ,.')
        return df.replace('', np.nan)
    else:
        df = df.fillna('')
        return df.str.lower().str.strip(' ,').replace('', np.nan)


def drop_columns_mentors(df):
    columns = ['Фамилия', 'Имя', 'Отчество',
       'Дата рождения', 'Дата создания', 'Другой телефон',
       'Другой e-mail', 'Должность',
       'Место работы/учёбы (полное наименование организации)',
       'Ассоциация выпускников - год выпуска',
       'Подразделение (факультет)', 'Подразделение факультет - Другое',
       'Ассоциация выпускников - Уровень квалификации',
       'Ассоциация выпускников - Ученая степень',
       'Ассоциация выпускников - Направление наставничества',
       'Ассоциация выпускников - Направление наставничества - Другое',
       'Ассоциация выпускников - Ваши интересы, умения, все, что хотите рассказать о себе',
       'Ассоциация выпускников - Направление, профиль',
       'Ассоциация выпускников - Какое учебное заведение окончили?',
       'Ассоциация выпускников - Какое учебное заведение окончили? (Другое)',
       'Ассоциация выпускников-Какой опыт в выбранном направлении наставничества имеете?.1',
       'Ассоциация выпускников - Какие навыки, компетенции вас характеризуют?',
       'Ассоциация выпускников - Чем можете помочь наставляемому?',
       'Ассоциация выпускников - Требования к наставляемому (если есть)']
    return df[columns]



def drop_columns_ank(df):
    columns = ['Дата создания',
               'Ф.И.О.',
               'Название лида',
                'Дата рождения',
                'Факультет и направление',
                'Уровень образования',
                'Форма оплаты за обучение',
                'Диплом с отличием',
                'Вы получали доп. образование во время обучения в РГГУ? (необязательно в подразделениях РГГУ)',
                'Доп. образование получено в РГГУ?',
                'Какое дополнительное образование Вы получили?',
                'Другое дополнительное образование Вы получили',
                'Планируете ли Вы продолжить образование?',
                'В получении какого образования Вы заинтересованы?',
                'Укажите другое (в получении какого образования Вы заинтересованы)?',
                'Планируете получать его в РГГУ?',
                'Где планируете получать образование?',
                'Как Вы оцениваете свой уровень образования, полученный в РГГУ?',
                'Как бы вы оценили уровень практической подготовки (практики)?',
                'Посоветовали бы Вы своим знакомым учиться в РГГУ?',
                'Указать другое (Посоветовали бы Вы своим знакомым учиться в РГГУ?)',
                'Есть ли у Вас опыт работы?',
                'Соответствует ли Ваша должность Вашей специальности?',
                'С какого курса Вы работаете?',
                'Примерный уровень зарплаты (в рублях)',
                'Вы работали по специальности?',
                'Оцените соответствие ваших знаний и навыков, полученных в процессе обучения, требованиям на вашей первой работе по специальности_выпуск',
                'Из каких источников вы узнали о приёме на работу?_выпуск',

                'Другое (Из каких источников Вы узнали о приёме на работу?)',
                'Где Вы работаете (планируете)?',
                'Другое (регион работы)',
                'Вы пойдете служить в армию?',
                'Какими мессенджерами пользуетесь?',
                'Какими соц.сетями Вы пользуетесь?',
                'Вы регулярно просматриваете их?',
                'Вы следите за сообществами РГГУ в социальных сетях?',
                'Форма обучения_выпуск',
                'Хотите ли вступить в Ассоциацию выпускников РГГУ?',
                'Нужна ли вам помощь специалистов Центра карьеры РГГУ или городской Службы занятости?_выпуск',

                'Рабочий телефон',
                'Рабочий e-mail',
                'Название компании',
                'Должность',            
                'Какими иностранными языками Вы владеете?',
                'Другие иностранные языки',
                'Ваше гражданство',
                'Гражданство указать',
                'Место жительства',
                'Место жительства указать',
                'Есть ли у Вас инвалидность',
                
                'Хотели бы вы получать рассылку от Центра карьеры РГГУ с вакансиями, стажировками и анонсами карьерных мероприятий?',
                'Хотели бы вы получать информацию об открытии наборов на обучение по программам профессиональной переподготовки и повышения квалификации в РГГУ?_выпуск']
                
    return df[columns]


def phone_correction(df, column: str):

    df[column] = df[column].replace(' ', '', regex=True)
    df[column] = df[column].replace('-', '', regex=True)
    df[column] = df[column].replace(r'\(', '', regex=True)
    df[column] = df[column].replace(r'\)', '', regex=True)
    df[column] = df[column].replace(r'\+', '', regex=True)
    df[column] = df[column].replace(r'\A7', r'8', regex=True)
    df[column] = df[column].replace(r';', r',', regex=True)
    df[column] = df[column].replace(r'\.', '', regex=True)
    df[column] = df[column].replace(r'/', '', regex=True)
    df[column] = df[column].replace(r'_', '', regex=True)
    df[column] = df[column].replace(r'^9', '89', regex=True)

def date_correction(df, column):
    if ' ' in df.loc[0, column]:
        df[column] = pd.to_datetime(df[column], format='%d.%m.%Y %H:%M:%S', dayfirst=True)
    else:
        df[column] = pd.to_datetime(df[column], format='%d.%m.%Y', dayfirst=True)



def name_col_mentor(df):

    df = df.rename(columns={'Другой телефон':'Телефон',
                                'Другой e-mail': 'Адрес электронной почты',
                                'Место работы/учёбы (полное наименование организации)': 'Место работы',
                                'Ассоциация выпускников - год выпуска': 'Год выпуска',
                                'Ассоциация выпускников - Уровень квалификации':'Уровень квалификации',
                                'Ассоциация выпускников - Ученая степень': 'Ученая степень',
                                'Ассоциация выпускников - Направление наставничества': 'Направление наставничества',
                                'Ассоциация выпускников - Ваши интересы, умения, все, что хотите рассказать о себе': 'Ваши интересы, умения, все, что хотите рассказать о себе',
                                'Ассоциация выпускников - Направление, профиль': 'Направление, профиль',
                                'Ассоциация выпускников - Какое учебное заведение окончили?': 'Какое учебное заведение окончили?',
                                'Ассоциация выпускников-Какой опыт в выбранном направлении наставничества имеете?.1': 'Какой опыт в выбранном направлении наставничества имеете?',
                                'Ассоциация выпускников - Какие навыки, компетенции вас характеризуют?': 'Какие навыки, компетенции вас характеризуют?',
                                'Ассоциация выпускников - Чем можете помочь наставляемому?': 'Чем можете помочь наставляемому?',
                                'Ассоциация выпускников - Требования к наставляемому (если есть)': 'Требования к наставляемому (если есть)'

            
        })
    
    return df


def drop_columns_menty(df):
    columns = ['Фамилия', 'Имя', 'Отчество',
                            'Дата рождения',
                            'Дата создания',
                            'Другой телефон',
                            'Другой e-mail',
                            'Курс (для студентов)',
                            'Подразделение (факультет)',
                            'Ассоциация выпускников - Направление, профиль',
                            'Ассоциация выпускников - Уровень образования',
                            'Ассоциация выпускников - Выберите, какой из вариантов больше подходит под ваш запрос наставнику',
                            'Ассоциация выпускников - Выберите, какой из вариантов больше подходит под ваш запрос наставнику - Другое',
                            'Ассоциация выпускников - Ваши сферы интересов',
                            'Ассоциация выпускников - Что вы хотите получить от наставничества',
                            'Ассоциация выпускников - Как вы видите своего наставника',
                            'Ассоциация выпускников - Предпочтительный формат взаимодействия с наставником',
                            'Ассоциация выпускников - Предпочтительный формат взаимодействия с наставником - Другое',
                            'Ассоциация выпускников - Оптимальное количество встреч']
    return df[columns]


def name_col_menty(df):

    df = df.rename(columns={'Другой телефон':'Телефон',
                            'Другой e-mail': 'Адрес электронной почты',
                            'Курс (для студентов)': 'Курс',
                            'Ассоциация выпускников - Направление, профиль': 'Направление, профиль',
                            'Ассоциация выпускников - Уровень образования': 'Уровень образования',
                            'Ассоциация выпускников - Выберите, какой из вариантов больше подходит под ваш запрос наставнику' : 'Выберите, какой из вариантов больше подходит под ваш запрос наставнику',
                            'Ассоциация выпускников - Выберите, какой из вариантов больше подходит под ваш запрос наставнику - Другое' : 'Выберите, какой из вариантов больше подходит под ваш запрос наставнику - Другое',
                            'Ассоциация выпускников - Ваши сферы интересов' : 'Ваши сферы интересов',
                            'Ассоциация выпускников - Что вы хотите получить от наставничества' : 'Что вы хотите получить от наставничества',
                            'Ассоциация выпускников - Как вы видите своего наставника': 'Как вы видите своего наставника',
                            'Ассоциация выпускников - Предпочтительный формат взаимодействия с наставником - Другое' : 'Предпочтительный формат взаимодействия с наставником - Другое',
                            'Ассоциация выпускников - Оптимальное количество встреч' : 'Оптимальное количество встреч',
                            'Ассоциация выпускников - Предпочтительный формат взаимодействия с наставником' : 'Предпочтительный формат взаимодействия с наставником'

            
        })
    
    return df

def citizenship_correction_ank(df, drop_col):

    new_dict_citizenship = {
    'российской федерациии':'россия',
    'российкая федерация':'россия',
    'российская федерация': 'россия',
    'россия': 'россия',
    'российская федерация': 'россия',
    'российская федерация':'россия', 
    'россии': 'россия',
    'рб':'беларусь',
    'молдова, республика':'молдова',
    'российская федерация':'россия',
    'сирийская арабская республика':'сирия',
    'иран, исламская республика':'иран',
    'корея, республика':'корея',
    'республика беларусь':'беларусь',
    'республика молдова':'молдова',
    'республика македония':'македония',
    'тайвань (китай)':'тайвань',
    'indonesia':'индонезия',
    'российское':'россия',
    'рф, казахстан':'россия, казахстан',
    'донецк':'днр',
    'туркменское':'туркменистан',
    'респулика абхазия':'абхазия',
    'латвийское':'латвия',
    'рф, вьетнам':'россия, вьетнам',
    'россия(туркменистан)':'россия, туркменистан',
    'мордовия': 'россия',
    'рф, бельгия':'россия, бельгия',
    'kz':'казахстан',
    'кыргызстан':'киргизия',
    'рф бельгия':'россия, бельгия',
    'россия, сирийская арабская республика':'россия, сирия',
    'республика южная осетия':'южная осетия',
    'абхазское':'абхазия',
    'сербское':'сербия',
    'боливия, многонациональное государство':'боливия',
    'россии':'россия',
    'румыния, молдова, республика':'румыния, молдова',
    'сербии':'сербия',
    'республика армения':'армения',
    'россия(эстония)':'россия, эстония',
    'республики таджикистан':'таджикистан',
    'молдова, республика, россия':'молдова, россия',
    'тайвань(taiwan)':'тайвань',
    'русское':'россия',
    'гражданин российской федерации':'россия',
    'российская федерации': 'россия',
    'алжира': 'алжир',
    'российской федерации':'россия',
    'русская':'россия',
    'рф': 'россия',
    'индонезий':'индонезия',
    'киргизская республика':'киргизия',
    'республика узбекистан':'узбекистан',
    'латвийское':'латвия',
    'туркменское':'туркменистан',
    'гватемале':'гватемала',
    ' республика беларусь':'беларусь',
    'литовской республики':'литва',
    'республика абхазия':'абхазия',
    'iran':'иран',
    'абхазское':'абхазия',
    'лучшее в мире - итальянское!':'италия',
    'тайвань(taiwan)':'тайвань',
    'киргизское':'киргизия',
    'македонка':'македония',
    'турецкое':'турция',
    'кыргызстан':'киргизия',
    'республика армения':'армения',
    'республика беларусь':'беларусь',
    'республика молдова':'молдова',
    'киргизии':'киргизия',
    'рб':'беларусь',
    ' республика беларусь':'беларусь',
    'республика казахстан':'казахстан',
    'ирана':'иран',
    'республика гватемала':'гватемала',
    'сербское':'сербия',
    'литовское':'литва',
    'республики таджикистан':'таджикистан',
    'армянское':'армения',
    'кнр':'китай',
    'македонское':'македония'}


    df['Гражданство указать'] = df['Гражданство указать'].replace(new_dict_citizenship)
    df['Ваше гражданство'] = df['Ваше гражданство'].replace(new_dict_citizenship)

    for i in range(len(df)):
        if df.loc[i, 'Ваше гражданство'] == 'иное':
            #если да, то вместо ИНОЕ записываем значение из 2 колонки
            df.loc[i, 'Ваше гражданство'] = df.loc[i, 'Гражданство указать']

    if drop_col:
        df = df.drop('Гражданство указать', axis=1)

    return df

    

def residence_correction_ank(df, drop_col): # ЗАМЕНИТЬ НА others!!!!!!!!!!!!!!!!!!!
    
    for i in range(len(df)):
        if df.loc[i, 'Место жительства'] == 'другой регион россии':
            #если да, то вместо ИНОЕ записываем значение из 2 колонки
            df.loc[i, 'Место жительства'] = df.loc[i, 'Место жительства указать']

    if drop_col:
        df = df.drop('Место жительства указать', axis=1)

    return df


def others(df, col_in: str, col_out: str, value_other: str, drop_col: bool):
    '''
    Функция меняет значения "иное", "другое" и т.п. на значения из следующего столбца

    col_in - название колонки, в которой есть "иное", "другое"
    col_out - название колонки, из которой надо взять значение на замену
    value_other - что именно заменяем ("иное", "другое" или что-то еще, само это слово)
    drop_col - удалять ли col_out. Если True, то да

    '''
    df = df.fillna('').reset_index(drop=True)

    for i in range(len(df)):
        if value_other in df.loc[i, col_in]:
            #если да, то вместо value_other записываем значение из col_out
            new_value = df.loc[i, col_out]
            df.loc[i, col_in] = re.sub(r'{}'.format(value_other), new_value, df.loc[i, col_in])
    
    if drop_col:
        df = df.drop(col_out, axis=1)

    return df.replace('', np.nan)


def language_correction(df, drop_col):

    for i in range(len(df)):
        df['Другие иностранные языки'] = df['Другие иностранные языки'].fillna('')
        if 'другие' in df.loc[i, 'Какими иностранными языками Вы владеете?']:
            #если да, то вместо ИНОЕ записываем значение из 2 колонки
            df.loc[i, 'Какими иностранными языками Вы владеете?'] = df.loc[i, 'Какими иностранными языками Вы владеете?'].replace('другие', df.loc[i, 'Другие иностранные языки'])   
    if drop_col:
        df = df.drop('Другие иностранные языки', axis=1)

    return df
    
def forma_ob_correction(df):
    df['Форма обучения_выпуск'] = df['Форма обучения_выпуск'].replace({'вечерняя':'очно-заочная', 'дневная':'очная'})


def id_find(df_to, df_from, col_to, col_from):

    '''
    Назначает идентификаторы из df_from в df_to на основе совпадений в указанных столбцах.

    Эта функция итерирует по каждой строке df_to и df_from, чтобы найти совпадения между указанными столбцами (col_to в df_to и col_from в df_from).
    Если находится совпадение, 'id' из df_from назначается соответствующей строке в df_to.
    Совпадения определяются наличием значения col_to из df_to внутри значения col_from из df_from, не обязательно точными совпадениями.
    Функция также обрабатывает отсутствующие значения, заполняя NaN пустыми строками перед сравнением.

    Параметры:

    df_to (pandas.DataFrame): Первый DataFrame, куда будет добавлен и обновлен столбец 'id' на основе совпадений.
    df_from (pandas.DataFrame): Второй DataFrame, из которого будут взяты значения 'id'.
    col_to (str): Название столбца в df_to для сравнения.
    col_from (str): Название столбца в df_from для сравнения с col_to в df_to.
    Возвращает:

    df_to (pandas.DataFrame): Обновленный DataFrame со столбцом 'id', добавленным/обновленным на основе совпадений.
    save_list_id (list): Список значений 'id', которые были назначены df_to на основе совпадений.

    
    '''
    df_to['id'] = ''
    df_to = df_to.fillna('')
    df_from = df_from.fillna('')
    save_list_id = []

    for i in range(len(df_to)):
        for j in range(len(df_from)):
            if ((df_to.loc[i, col_to] != '') and (df_to.loc[i, col_to] is not np.nan)) and (df_to.loc[i, col_to] in df_from.loc[j, col_from]):
                save_list_id.append(df_from.loc[j, 'id'])
                df_to.loc[i, 'id'] = df_from.loc[j, 'id'] 

    return df_to, save_list_id


def add_new_row_to_fiz_from_ank(df_ank_id, df_fiz):
    """
    Добавляет новые строки в DataFrame df_fiz из другого DataFrame df_ank_id на основе определенных условий.
    
    Функция проходит по строкам df_ank_id и для каждой строки, где 'id' равен пустой строке (то есть отсутствует), 
    создает новую строку в df_fiz с уникальным 'id', а также копирует значения 'Ф.И.О.', 'Дата рождения' и 
    вычисляет 'birthday_year' из 'Дата рождения'. Это предназначено для обновления таблицы с данными физических лиц, 
    добавляя новых людей из списка анкет. Так же мы удаляем из df_ank_id дубликаты по ФИО, чтобы не добавить в физлица
    одного и того же человека два раза. Нужно убедиться, что среди дублей нет полных тезок.

    Мы добавляем ФИО, id и дату рождения, чтобы потом сопоставить их с файлом анкет и добавить всю информацию по этим id.

    Параметры:
        df_ank_part (pandas.DataFrame): DataFrame, содержащий данныe анкеты с частично отсутствующими id.
        df_fiz (pandas.DataFrame): DataFrame, куда будут добавлены новые строки, содержащий основные данные физических лиц.

    Возвращает:
        pandas.DataFrame: Обновленный DataFrame df_fiz с добавленными новыми строками.
    
    Побочные эффекты:
        Модифицирует переданный DataFrame df_fiz путем добавления новых строк.

    """
    df_new = df_ank_id[df_ank_id['id'] == ''].drop_duplicates('Ф.И.О.').copy()
    df_new['Дата рождения'] = df_new['Дата рождения'].astype('str')
    max_id = df_fiz.id.astype('int').max()
    max_index = df_fiz.index.max()

    for _, row in df_new.iterrows():
        new_index = max_index + 1
        df_fiz.loc[new_index, 'id'] = max_id + 1
        df_fiz.loc[new_index, 'fio'] = row['Ф.И.О.']
        df_fiz.loc[new_index, 'birthday'] = str(row['Дата рождения'])
        df_fiz.loc[new_index, 'birthday_year'] = str(row['Дата рождения'])[:4]
        df_fiz.loc[max_index+1, 'Email'] = row['Рабочий e-mail']

        max_id += 1
        max_index += 1

    return df_fiz



def ank_to_fiz(df_to, df_from, col_to, col_from, on='id', association_member = False):
    """
    Объединяет значения в двух pandas DataFrame по совпадающим идентификаторам и уникально объединяет значения в указанных столбцах.

    Параметры:
    - df_to (pandas.DataFrame): DataFrame, в который будут добавляться значения. Должен содержать столбец 'id'.
    - df_from (pandas.DataFrame): DataFrame, из которого будут извлекаться значения. Должен содержать столбец 'id'.
    - col_to (str): Название столбца в df_to, в который будут добавлены уникальные значения из df_from.
    - col_from (str): Название столбца в df_from, из которого будут извлекаться значения для добавления в df_to.

    Описание работы:
    1. Преобразует тип данных столбца 'id' в обоих DataFrame в 'int' для удобства сравнения.
    2. Заполняет все NaN значения в обоих DataFrame пустой строкой, чтобы избежать проблем с типами данных при операциях.
    3. Итерирует через каждую строку в df_to и df_from, сравнивая значения 'id'. Если 'id' совпадают, функция объединяет значения из col_from и col_to, удаляя дубликаты.
    4. Результаты сохраняются в col_to df_to.

    Возвращаемое значение:
    - pandas.DataFrame: Обновленный DataFrame df_to с уникально объединенными значениями в указанном столбце col_to.

    """
    df_from = df_from.fillna('').reset_index(drop=True)
    df_to = df_to.fillna('').reset_index(drop=True)

    if on == 'id':
        df_to.id = df_to.id.astype('int')
        df_from.id = df_from.id.astype('int')

        for i in range(len(df_to)):
            for j in range(len(df_from)):
                if df_to.loc[i, on] == df_from.loc[j, on]:
                    str_ = df_from.loc[j, col_from] + ',' + df_to.loc[i, col_to]
                    split_ = str_.split(',')
                    df_to.loc[i, col_to] = ','.join(set(split_)).replace(',,', ',').strip(' ,.')
                    if association_member == True:
                        str_ = 'член ассоциации выпускников' + ',' + df_to.loc[i, 'status']
                        split_ = str_.split(',')
                        df_to.loc[i, 'status'] = ','.join(set(split_)).replace(',,', ',').strip(' ,.')

        return df_to
    
    else:
        for i in range(len(df_to)):
            for j in range(len(df_from)):
                if df_from.loc[j, on] in df_to.loc[i, on]:
                    str_ = df_from.loc[j, col_from] + ',' + df_to.loc[i, col_to]
                    split_ = str_.split(',')
                    df_to.loc[i, col_to] = ','.join(set(split_)).replace(',,', ',').strip(' ,.')
                    if association_member == True:
                        str_ = 'член ассоциации выпускников' + ',' + df_to.loc[i, 'status']
                        split_ = str_.split(',')
                        df_to.loc[i, 'status'] = ','.join(set(split_)).replace(',,', ',').strip(' ,.')

        return df_to



def unsubscribe(df_to, df_from, col_to, col_from, mark):
    """
    Обновляет значения в столбце col_to DataFrame df_to на основе совпадений значений в столбце 'id'
    и условий в столбце col_from DataFrame df_from. Если в df_from в столбце col_from стоит значение 'нет'
    для совпадающего 'id', к значению в df_to в col_to добавляется метка 'mark', избегая дубликатов.

    Параметры:
    df_to (pandas.DataFrame): DataFrame, в который будут внесены изменения.
    df_from (pandas.DataFrame): DataFrame, из которого берутся условия для обновления df_to.
    col_to (str): Название столбца в df_to, куда добавляется метка.
    col_from (str): Название столбца в df_from, содержащего условия ('нет') для добавления метки.
    mark (str): Метка, добавляемая к значению в col_to, если условие выполнено.

    Возвращает:
    pandas.DataFrame: Обновленный df_to с добавленными метками в столбец col_to при выполнении условий.

    """
    df_to.id = df_to.id.astype('int')
    df_from.id = df_from.id.astype('int')
    df_from = df_from.fillna('')
    df_to = df_to.fillna('')

    for i in range(len(df_to)):
        for j in range(len(df_from)):
            if df_to.loc[i, 'id'] == df_from.loc[j, 'id']:
                if df_from.loc[j, col_from] == 'нет':
                    str_ = df_to.loc[i, col_to] + ',' + mark
                    split_ = set(str_.split(','))
                    value_ = ','.join(split_).strip(',').replace(',,', ',')
                    df_to.loc[i, col_to] = value_

    return df_to




def extract_year(value_: datetime) -> int:
 
    """
    Функция извлекает год из даты.
    """

    value_ = value_.year
    return value_

