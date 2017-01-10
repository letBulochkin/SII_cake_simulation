from cook import *


def set_params(c):
    print('Установите параметры повара:')
    c.knife = bool(int(input('Наличие ножа:')))
    if bool(input('Наличие формы:')):
        c.form = Form()
    c.plate = bool(int(input('Наличие емкости:')))
    c.oven = bool(int(input('Наличие печи:')))
    c.timer = int(input('Значение таймера (<30):'))
    print('Значения атрибутов класса:')
    print(c.__dict__)
    return c


def main():
    print('Симуляция приготовления пирога.')
    the_cook = Cook()
    the_cook = set_params(the_cook)
    while True:
        i = int(input("""
        Выберите действие:
        1 - Купить ингредиенты
        2 - Разбить яйца
        3 - Отделить желток и белок
        4 - Приготовить сметанно-желтковую смесь
        5 - Взбить белки
        6 - Приготовить массу
        7 - Нарезать сыр
        8 - Вымыть, почистить, нарезать груши
        9 - Разморозить тесто
        10 - Поместить ингредиенты в форму
        11 - Выпечь пирог
        12 - Убедиться в готовности пирога
        0 - Выход
        """))
        try:
            if i == 1:
                batter = Batter()
                pears = Pears()
                eggs = Eggs()
                sour = SourCream()
                cheese = Cheese()
                the_cook.buy(batter)
                the_cook.buy(pears)
                the_cook.buy(eggs)
                the_cook.buy(sour)
                the_cook.buy(cheese)
            elif i == 2:
                the_cook.break_egg(eggs)
            elif i == 3:
                white, yellow = the_cook.split_egg(eggs)
            elif i == 4:
                sour_mix = the_cook.mix_ingerds(yellow, sour)
            elif i == 5:
                the_cook.whip(white)
            elif i == 6:
                mass = the_cook.mix_ingerds(white, sour_mix)
            elif i == 7:
                the_cook.cut(cheese)
            elif i == 8:
                the_cook.wash(pears)
                the_cook.clean(pears)
                the_cook.cut(pears)
            elif i == 9:
                the_cook.defreeze(batter)
            elif i == 10:
                the_cook.place(batter, the_cook.form)
                the_cook.place(pears, batter)
                the_cook.place(mass, pears)
                the_cook.place(cheese, mass)
            elif i == 11:
                cake = the_cook.bake([batter, pears, mass, cheese])
            elif i == 12:
                the_cook.finish_cooking(cake)
            elif i == 0:
                break
        except UnboundLocalError:
                    print('Не все компоненты действия существуют!')


if __name__ == "__main__":
    main()