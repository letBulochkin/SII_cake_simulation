from ingredients import *


class Cook:
    def __init__(self):
        self.knife = None
        self.form = None
        self.plate = None
        self.oven = None
        self.timer = 0
        print('Повар готов к приготовлению блюда.')

    def buy(self, ingred):
        ingred.bought = True
        print('Куплен:', ingred.name)

    def break_egg(self, egg):
        if self.knife:
            egg.broken = True
            print('Разбито:', egg.name)
        else:
            print('Ошибка! Нет компонента действия: Нож')

    def split_egg(self, egg):
        w, y = egg.eggsplit()
        print('Разделено:', egg.name)
        return w, y

    def mix_ingerds(self, ing1, ing2):
        if self.plate:
            if isinstance(ing1, Yellow) and isinstance(ing2, SourCream):
                sm = SourMixture()
                print('Cмешаны объекты:', ing1.name, ',', ing2.name)
                return sm
            if isinstance(ing1, White) and isinstance(ing2, SourMixture):
                ms = Mass()
                print('Cмешаны объекты:', ing1.name, ',', ing2.name)
                return ms
        else:
            print('Ошибка! Нет компонента действия: Емкость')

    def whip(self, wh):
        if self.plate:
            print('Взбиты:', wh.name)
            wh.whipped = True
        else:
            print('Ошибка! Нет компонента действия: Емкость')

    def cut(self, ing):
        if self.knife:
            print('Нарезан:', ing.name)
            ing.cut = True
        else:
            print('Ошибка! Нет компонента действия: Нож')

    def wash(self, ing):
        print('Вымыт:', ing.name)
        ing.washed = True

    def clean(self, ing):
        if self.knife:
            print('Очищен:', ing.name)
            ing.cleaned = True
        else:
            print('Ошибка! Нет компонента действия: Нож')

    def defreeze(self, ing):
        print('Разморожен:', ing.name)
        ing.defreezed = True

    def place(self, ing, onto):
        try:
            print('Объект:', ing.name, 'Помещен в:', onto.name)
            ing.placed = True
            onto.covered = True
        except AttributeError:
            print('Ошибка! Нет компонента действия')
        '''
        ing.placed = True
        onto.covered = True
        '''

    def bake(self, ingreds):
        if self.form:
            if self.form.covered:
                for i in ingreds:
                    if not i.placed:
                        print('Объект:', i.name, 'не помещен!')
                        return
                c = Cake()
                print('Запущен таймер выпечки!')
                while self.timer < 30:
                    print('Значение таймера:', self.timer)
                    self.timer += 1
                c.crust = True
            else:
                print('Форма не заполнена!')
                return
        else:
            print('Ошибка! Нет компонента действия: Форма')
        if c.crust:
            c.baked = True
            print('Испечен:', c.name)
            return c
        else:
            print('Пирог не испечен!')
            return c

    def finish_cooking(self, cake):
        if cake.baked:
            cake.done = True
            print('Готов:', cake.name)
        else:
            print('Ошибка! Не готов:', cake.name)
