import datetime, random, os


questions = ["Что вы видите на картинке?", "Какие чувства у вас вызывает картинка?", "Где вы на этой картинке?",
                     "Как изображение на картинке отзывается в вашем теле?",
                     "Какие ассоциации вызывает у вас эта картинка?",
                     "Как изображение на картинке связано с вашим запросом?",
                     "Что может помочь вам справиться с ситуацией, описанной в вашем запросе?"]

def main_menu(a):
    print('\n"Метафорические Карты" ver. 0.9.99')
    print('Доступные опции: \n"Старт" \n"Выход"\n')
    while True:
        usr_inp = input('Ввод :').lower()
        if usr_inp == 'старт':
            a += 1
            return a
        elif usr_inp == 'выход':
            print('Работа программы завершена.')
            a -= 1
            return a
        else:
            print('Некорректный ввод.\n')

def progression_movement(a, b):
    if a.lower() == 'назад':
        b -= 1
    else:
        b += 1
    return b

def name_inp(a):
    print('Доступные опции: \n"Назад"')
    while True:
        usr_name = input('\nВведите ваше имя :')
        if len(usr_name) >= 1:
            a = progression_movement(usr_name, a)
            break
        else:
            print('Слишком короткое имя пользователя.')
    return a, usr_name

def theme_inp(a):
    print('Доступные опции: \n"Назад"')
    while True:
        theme = input('\nСформулируйте ваш запрос. Опишите, что именно вас беспокоит. Ввод :')
        if len(theme) >= 1:
            a = progression_movement(theme, a)
            break
        else:
            print('\nЗапрос отсутствует.')
    return a, theme

def card_choice(a):
    while True:
        print('\nВыберите номер карты. \nДоступные опции: \n"Указать вручную" \n"Случайная карта"\n"Назад"')
        card = input('Ввод :').lower()
        if card == 'назад':
            a -= 1
            card_num = 0
            break
        elif card == 'указать вручную':
            card_num = input('\nВведите номер карты в диапазоне от 1 до 88. Ввод :')
            try:
                card_num = int(card_num)
                if 1 <= card_num <= 88:
                    a += 1
                    break
                else:
                    print('Указанный номер карты не соответствует предложенному диапазону.')
            except ValueError:
                print('Некорректный формат ввода. Укажите число, например, "5" или "42".')
        elif card == 'случайная карта':
            card_num = random.randint(1, 88)
            a += 1
            break
        else:
            print('\nНекорректный ввод.\n')
    return a, card_num

def card_number_correction(a):
    a = str(a)
    if len(a) == 1:
        a = '00' + a
    elif len(a) == 2:
        a = '0' + a
    elif len(a) > 2:
        a = '0' + a[-2::]
    return a

def questionnaire(a, b, c):
    question_number = 1
    answers = dict()
    b = card_number_correction(b)
    os.startfile(f'cards\\{b}.jpg')
    print('\nЭтап работы с картой. \nОтветьте на вопрос ниже. \n')
    while True:
        print('\nДоступные опции: \n"Назад"\n"Другой вопрос" \n"Завершить"\n')
        answer = input(f'{c[question_number]} \nВвод: ').lower()
        if len(answer) > 0:
            if answer == 'назад':
                a -= 1
                break
            elif answer == 'другой вопрос':
                if question_number == 6:
                    print('Доступные вопросы закончились.')
                else:
                    question_number += 1
                continue
            elif answer == 'завершить':
                a += 1
                break
            answers[c[question_number]] = answer
            print('Ответ принят! \n')
        else:
            print('Ответ отсутствует.')
    return a, answers

def results(a, b, c, d, e):
    print('Благодарим за использование программы! \nЖелаете сохранить результаты в файл? ("Да" / "Нет")\n')
    while True:
        usr_inp = input('Ввод :').lower()
        if usr_inp != 'да' and usr_inp != 'нет':
            print('Некорректный ввод.\n')
            continue
        if usr_inp == 'да':
            with open(f"{b}_{datetime.datetime.strftime(datetime.datetime.now(), format='%Y-%m-%d %H-%M')}.txt",'w', encoding='utf8') as f:
                f.write(f'Имя пользователя: {b} \n')
                f.write(f'Запрос: {c} \n')
                f.write(f'Номер картинки: {d}. \n')
                for i in list(e.keys()):
                    f.write(f'\nВопрос: {i} \nОтвет: {e[i]}')
            print('Результаты сохранены!')
        a = 0
        break
    return a

def metaphor_cards(a):

    question_list = a
    progress = 0
    usr_name = str()
    theme = str()
    card_num = 0
    answers = dict()

    while True:
        if progress == -1:
            break
        if progress == 0:
            progress = main_menu(progress)
        if progress == 1:
            progress, usr_name = name_inp(progress)
        if progress == 2:
            progress, theme = theme_inp(progress)
        if progress == 3:
            progress, card_num = card_choice(progress)
        if progress == 4:
            progress, answers = questionnaire(progress, card_num, question_list)
        if progress == 5:
            progress = results(progress, usr_name, theme, card_num, answers)

metaphor_cards(questions)



