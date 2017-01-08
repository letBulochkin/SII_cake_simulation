from ingredients import *


class Cook:
    def __init__(self):
        self.knife = True
        self.form = Form()
        self.plate = True
        self.oven = True
        self.timer = 0
        print('Повар готов к приготовлению блюда.')

    def buy(self, ingred):
        ingred.bought = True
        print('Куплен:', ingred.name)

    def break_egg(self, egg):
        egg.broken = True
        print('Разбито:', egg.name)

    def split_egg(self, egg):
        w, y = egg.eggsplit()
        print('Разделено:', egg.name)
        return w, y

    def mix_ingerds(self, ing1, ing2):
        print('Cмешаны объекты:', ing1.name, ',', ing2.name)
        if str(type(ing1)) == "<class 'ingredients.Yellow'>" and str(type(ing2)) == "<class 'ingredients.SourCream'>":
            sm = SourMixture()
            return sm
        elif str(type(ing1)) == "<class 'ingredients.White'>" and str(type(ing2)) == "<class 'ingredients.SourMixture'>":
            ms = Mass()
            return ms

    def whip(self, wh):
        print('Взбиты:', wh.name)
        wh.whipped = True

    def cut(self, ing):
        print('Нарезан:', ing.name)
        ing.cut = True

    def wash(self, ing):
        print('Вымыт:', ing.name)
        ing.washed = True

    def clean(self, ing):
        print('Очищен:', ing.name)
        ing.cleaned = True

    def defreeze(self, ing):
        print('Разморожен:', ing.name)
        ing.defreezed = True

    def place(self, ing, onto):
        print('Объект:', ing.name, 'Помещен в:', onto.name)
        ing.placed = True
        onto.covered = True

    def bake(self, ingreds):
        if self.form.covered:
            for i in ingreds:
                if not i.placed:
                    print('Объект:', i.name, 'не помещен!')
                    return
        else:
            print('Форма не заполнена!')
            return
        c = Cake()
        print('Запущен таймер выпечки!')
        while self.timer < 30:
            print('Значение таймера:', self.timer)
            self.timer += 1
        c.crust = True
        c.baked = True
        print('Испечен:', c.name)
        return c

    def finish_cooking(self, cake):
        if cake.crust:
            cake.done = True
            print('Готов:', cake.name)
