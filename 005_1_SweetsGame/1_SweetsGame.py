# Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

import random

import os

def GetNumb(x, turnMax):
    if x > turnMax:
        a = input('Введите число от 1 до 28 \n')
        while int(a) not in range(1, turnMax+1):
            a = input('Введите число от 1 до 28 \n')
        return int(a)
    else:
        a = input(f'Введите число от 1 до {x} \n')
        while int(a) not in range(1, x+1):
            a = input(f'Введите число от 1 до {x} \n')
        return int(a)

def ModeSelection():
    a = input('выбор режима: \n1 - два игрока \n2 - игрок - компьютер лёгкий \n3 - игрок - компьютер профи\n')
    while int(a) not in range(1, 4):
        a = input('выбор режима: \n1 - два игрока \n2 - игрок - компьютер \n3 - игрок - компьютер профи\n')
    return int(a)

def Mode_UserVsEasyBot(SweetsQty, User1, turnMax, turnMin):
    print((lambda x: "игрок ходит первым" if x ==
           1 else "компьютер ходит первым")(User1))
    print(f'остаток {SweetsQty}')
    while SweetsQty > 0:
        if User1 == True:
            print('Ход игрока')
            SweetsQty -= GetNumb(SweetsQty, turnMax)
            User1 = not User1
            os.system('cls')
            print(f'остаток {SweetsQty}')
        else:
            print('Ход компьютера')
            if turnMin <= SweetsQty <= turnMax:
                compTurn = random.randint(1, SweetsQty)
                SweetsQty -= compTurn
                User1 = not User1
                print(f'{compTurn} \nостаток {SweetsQty}')
            else:
                compTurn = random.randint(1, 29)
                SweetsQty -= compTurn
                User1 = not User1
                print(f'{compTurn} \nостаток {SweetsQty}')
    if User1 == False:
        return print('Победил игрок\nКОНЕЦ')
    else:
        return print('Победил компьютер\nКОНЕЦ')

def Mode_UserVsUser(SweetsQty, User1, turnMax):
    print((lambda x: "1й игрок ходит первым" if x ==
           1 else "2й игрок ходит первым")(User1))
    print(f'остаток {SweetsQty}')
    while SweetsQty > 0:
        if User1 == True:
            print('Ход 1го игрока')
            SweetsQty -= GetNumb(SweetsQty, turnMax)
            User1 = not User1
            os.system('cls')
            print(f'остаток {SweetsQty}')
        else:
            print('Ход 2го игрока')
            SweetsQty -= GetNumb(SweetsQty, turnMax)
            User1 = not User1
            os.system('cls')
            print(f'остаток {SweetsQty}')
    if User1 == False:
        print('Победил 1й игрок\nКОНЕЦ')
    else:
        print('Победил 2й игрок\nКОНЕЦ')

def intDivision(x, y):
    if x%y == 0: return (y//2)
    else: return x%y

def Mode_UserVsHardBot(SweetsQty, User1, turnMax, turnSum):
    os.system('cls')
    print((lambda x: "игрок ходит первым" if x ==
           1 else "компьютер ходит первым")(User1))
    print(f'остаток {SweetsQty}')
    if User1 == 0:
        for i in range(0, (SweetsQty//turnSum)+1):
            if i == 0:
                print(f'ход компьютера - {intDivision(SweetsQty, turnSum)}')
                SweetsQty -= (intDivision(SweetsQty, turnSum))
                print(f'остаток - {SweetsQty} \nход игрока')
                usturn = GetNumb(SweetsQty, turnMax)
                SweetsQty -= usturn
                print(f'остаток {SweetsQty}')
            else:
                SweetsQty -= (turnSum - usturn)
                print(
                    f'ход компьютера - {turnSum - usturn} \nостаток - {SweetsQty}')
                if SweetsQty == 0:
                    break
                print('ход игрока')
                usturn = GetNumb(SweetsQty, turnMax)
                SweetsQty -= usturn
                print(f'остаток {SweetsQty}')
        print('Победил компьютер\nКОНЕЦ')
    else:
        for i in range(0, (SweetsQty//turnSum)+1):
            print('ход игрока')
            usturn = GetNumb(SweetsQty, turnMax)
            SweetsQty -= usturn
            print(f'остаток {SweetsQty}')
            User1 = not User1
            if SweetsQty == 0:
                break
            if intDivision(SweetsQty, turnSum) != 0:
                print(f'ход компьютера - {intDivision(SweetsQty, turnSum)}')
                SweetsQty -= (intDivision(SweetsQty, turnSum))
                print(f'остаток - {SweetsQty}')
                User1 = not User1
                if SweetsQty == 0:
                    break
            else:
                SweetsQty -= (turnSum - usturn)
                print(
                    f'ход компьютера - {turnSum - usturn} \nостаток - {SweetsQty}')
                User1 = not User1
                if SweetsQty == 0:
                    break
        if User1 == 1:
            print('Победил компьютер\nКОНЕЦ')
        else:
            print('Победил игрок\nКОНЕЦ')

SweetsQty = 221
turnMax = 28
turnMin = 1
turnSum = turnMin + turnMax
User1 = bool(random.randint(False, True))
select = ModeSelection()
if select == 1:
    Mode_UserVsUser(SweetsQty, User1, turnMax)
elif select == 2:
    Mode_UserVsEasyBot(SweetsQty, User1, turnMax, turnMin)
elif select == 3:
    Mode_UserVsHardBot(SweetsQty, User1, turnMax, turnSum)

