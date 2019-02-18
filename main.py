from random import randint as rnd
import os

korol = {'ЗЕРНО': 10500, 'НАРОД': 100, 'ЗЕМЛЯ': 150, 'КАЗНА': 10000, 'СМУТА': 10, 'ГОД': 0}


def write(dct):
    os.system('clear')
    for i in dct:
        print(i, end=' ')
    print('\n')
    for i in dct:
        print(dct[i], end='   ')


def buy(p):
    b = int(input('Сколько зерна купить?'))
    if korol['КАЗНА'] < (p * b):
        b = int(input('Недостаточно средств, введите новое значение: '))
    korol['ЗЕРНО'] = korol['ЗЕРНО'] + b
    korol['КАЗНА'] = korol['КАЗНА'] - (p * b)


def gamesituation(situation):
    if situation == 1:
        print("Ваши амбары наполнили полчища крыс!!!")
        korol['ЗЕРНО'] = korol['ЗЕРНО'] - rnd(500, 1000)

    elif situation == 2:
        bo = bool(input("началась война, объявить мобилизацию?"))
        if bo:
            war = rnd(10, 30)
            korol['НАРОД'] = korol['НАРОД'] - war
            korol['СМУТА'] = korol['СМУТА'] + war
            final = rnd(1, 2)
            ert = rnd(30, 50)
            if final == 1:
                print('Вы проиграли в войне, и отдаете', ert, 'земли')
                korol['ЗЕМЛЯ'] = korol['ЗЕМЛЯ'] + ert
            else:
                print('Вы выиграли в войне, и получаете', ert, 'земли')
                korol['ЗЕМЛЯ'] = korol['ЗЕМЛЯ'] - ert
        else:
            print('Вы проиграли в войне, и отдаете', ert, 'земли')
            korol['ЗЕМЛЯ'] = korol['ЗЕМЛЯ'] - ert

    elif situation == 3:
        pres = rnd(5000, 10000)
        print('После долгой болезни скончался ваш дальний родственник, в наследство вам досталось', pres)
        korol['КАЗНА'] = korol['КАЗНА'] + pres
    input("Нажмите Enter чтобы продолжить...")


def game(price, n):
    sell = int(input('Сколько зерна продать? '))
    if sell > korol['ЗЕРНО']:
        sell = int(input('Недостаточно зерна, введите новое значение: '))
    korol['ЗЕРНО'] = korol['ЗЕРНО'] - sell
    korol['КАЗНА'] = korol['КАЗНА'] + (price * sell)
    sow = int(input('Сколько зерна выделить на посев? '))
    if sow > korol['ЗЕРНО']:
        sow = int(input('Недостаточно зерна, введите новое значение: '))
    korol['ЗЕРНО'] = korol['ЗЕРНО'] - sow
    korol['ЗЕМЛЯ'] = korol['ЗЕМЛЯ'] - (sow // 100)
    giv = int(input('Сколько зерна раздать подданным? '))
    if giv > korol['ЗЕРНО']:
        giv = int(input('Недостаточно зерна, введите новое значение: '))
    korol['ЗЕРНО'] = korol['ЗЕРНО'] - giv
    if giv <= 1000:
        korol['НАРОД'] = korol['НАРОД'] - n
        korol['СМУТА'] = korol['СМУТА'] + n
    elif giv >= 1000:
        korol['НАРОД'] = korol['НАРОД'] + n
        korol['СМУТА'] = korol['СМУТА'] - n
    korol['ГОД'] = korol['ГОД'] + 1


while korol['НАРОД'] > 0 and korol['СМУТА'] > 0 and korol['ЗЕМЛЯ'] > 0:
    write(korol)
    x = rnd(1, 3)
    y = rnd(1, 3)
    price = rnd(25, 40)
    pricebuy = rnd(30, 60)
    n = rnd(1, 2)
    if x == 1:
        print('\n\nНегоциант из Голландии купит зерна по', price, 'золотых за бушель')
        game(price, n)
        print('Торговый союз продаст зерна по', pricebuy, 'золотых за бушель')
        buy(pricebuy)
        gamesituation(y)

    if x == 2:
        print('\n\nТорговый союз купит зерна по', price, 'золотых за бушель')
        game(price, n)
        print('Русский царь продаст зерна по', pricebuy, 'золотых за бушель')
        buy(pricebuy)
        gamesituation(y)

    if x == 3:
        print('\n\nРусский царь купит зерна по', price, 'золотых за бушель')
        game(price, n)
        print('Негоциант из Голландии продаст зерна по', pricebuy, 'золотых за бушель')
        buy(pricebuy)
        gamesituation(y)

if korol['НАРОД'] <= 0 or korol['ЗЕМЛЯ'] <= 0:
    print(
        'Население не может больше терпеть вашего бездарного правления\nВы низложны!!!Жалкий интриган, время вашего правления составило',
        korol['ГОД'])
elif korol['СМУТА'] <= 0:
    print('Население восхваляет вас, вы лучший царь за всю историю, время вашего правления составило', korol['ГОД'])

