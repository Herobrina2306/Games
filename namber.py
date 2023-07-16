import random 

name = input("Пожалуйста представься: ") 
print(f'Привет {name}. Давай поиграем.')

vare = 'да' 

def namber_game():
    
    i = 0
    
    diap = random.randint(1, 80)

    result = random.randint(diap, diap+20)
    
    print(f'''Я загадал число от {diap} до {diap+20}. 
          Попробуйте угадать. Начнём. 
          Введите число: ''') 
    
    while i < 7:
        namber = int(input())
        if namber == result:
            i += 1
            print(f'Вы угадали! Количество ходов = {i}. \nЯ загадал число {result}.')
            break
        elif namber > result:
            print ('Не-а. Моё число меньше') 
            i += 1
        elif namber < result:
            print ('Не угадал. Моё число больше ') 
            i += 1
        
    if i == 7:
        print (f'''У вас к сожалению закончились попытки. 
               Я загадывал число, {result}''') 
        
while vare == 'да' or vare == 'д' or vare == 'Да':
    namber_game()
    vare = input('Хотите сыграть ещё? Да или нет? \n')
    
    
    