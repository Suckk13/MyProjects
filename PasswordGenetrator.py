#password_generator by realcode.cc
#файлы для работы и настройки, НЕ ТРОГАТЬ ВСЕ СЛОМАЕТСЯ
import random
file = open('Passwords.txt', 'a+')
file.read()
saving_password = {

}
feedback = """
            Help - справка
            Add  - Добавить пароль
            Show - показать список паролей
            Quit - выход из программы и сохранение всех паролей"""
print(feedback)
programm_is_run = True
#Основной код
while programm_is_run:
    command = input('Введите команду\n')
    command = command.lower()

    #quit
    if command == 'quit':
        print('Выход из программы...')
        exit()
    # help command
    elif command == 'help':
        print(feedback)

    #show command
    elif command == 'show':
        print(saving_password)
    #add  command
    elif command == 'add':
        password = ''
        lenght = int(input('Введите длинну пароля: '))

        for x in range(lenght):
            password += random.choice(('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
        print('Сгенерированный пароль: ', password)
        app = input('Для какого приложения вы хотите его использовать? ')
        complete = saving_password.update({app: password})
        key_password = list(saving_password.keys())[-1]
        app_password = list(saving_password.values())[-1]
        complete2 = str(key_password + ':' + app_password)
        file.write(complete2)
        file.write('\n')
    else:
        print('Команда не найдена')
file.close()
