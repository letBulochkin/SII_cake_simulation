from cook import *

batter = Batter()
pears = Pears()
eggs = Eggs()
sour = SourCream()
cheese = Cheese()

the_cook = Cook()

the_cook.buy(batter)
the_cook.buy(pears)
the_cook.buy(eggs)
the_cook.buy(sour)
the_cook.buy(cheese)

the_cook.break_egg(eggs)

white, yellow = the_cook.split_egg(eggs)

sour_mix = the_cook.mix_ingerds(yellow, sour)

the_cook.whip(white)

mass = the_cook.mix_ingerds(white, sour_mix)

the_cook.cut(cheese)

the_cook.wash(pears)
the_cook.clean(pears)
the_cook.cut(pears)

the_cook.defreeze(batter)

the_cook.place(batter, the_cook.form)
the_cook.place(pears, batter)
the_cook.place(mass, pears)
the_cook.place(cheese, mass)

cake = the_cook.bake([batter, pears, mass, cheese])

the_cook.finish_cooking(cake)
