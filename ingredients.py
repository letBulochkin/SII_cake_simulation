class SourCream:
    def __init__(self):
        self.bought = False
        self.name = 'Сметана'
        print('Создан объект:', self.name)


class Eggs:
    def __init__(self):
        self.bought = False
        self.split = False
        self.broken = False
        self.name = 'Яйца'
        print('Создан объект:', self.name)

    def eggsplit(self):
        self.split = True
        w = White()
        y = Yellow()
        self.__del__()
        return w, y

    def __del__(self):
        print('Объект уничтожен:', self.name)


class White:
    def __init__(self):
        self.whipped = False
        self.name = 'Белки'
        print('Создан объект:', self.name)


class Yellow:
    def __init__(self):
        self.name = 'Желтки'
        print('Создан объект:', self.name)


class SourMixture:
    def __init__(self):
        self.name = 'Яично-сметанная смесь'
        print('Создан объект:', self.name)


class Form:
    def __init__(self):
        self.covered = False
        #self.pear_covered = False
        #self.mass_covered = False
        #self.cheese_covered = False
        self.name = 'Форма для выпечки'
        print('Создан объект:', self.name)


class Batter:
    def __init__(self):
        self.placed = False
        self.covered = False
        self.defreezed = False
        self.bought = False
        self.name = 'Тесто'
        print('Создан объект:', self.name)


class Pears:
    def __init__(self):
        self.placed = False
        self.cut = False
        self.covered = False
        self.cleaned = False
        self.washed = False
        self.bought = False
        self.name = 'Груши'
        print('Создан объект:', self.name)


class Mass:
    def __init__(self):
        self.placed = False
        self.mixed = False
        self.covered = False
        self.name = 'Масса'
        print('Создан объект:', self.name)


class Cheese:
    def __init__(self):
        self.placed = False
        self.cut = False
        self.bought = False
        self.name = 'Сыр'
        print('Создан объект:', self.name)


class Cake:
    def __init__(self):
        self.done = False
        self.baked = False
        self.crust = False
        self.placed = False
        self.name = 'Пирог'
        print('Создан объект:', self.name)
