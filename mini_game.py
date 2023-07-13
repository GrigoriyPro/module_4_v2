import random
class Fighter:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.damage = 20

    def atack(self, other):
        other.hp -= self.damage

voini = [Fighter("Геракл", 100),Fighter("Бык", 100)]

print("Кто-же победит?!")

while True:

    i = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите любую цифру: ')

    if i == '1':

        gg = random.randint(0, 1)
        attacker = voini[gg]
        defender = voini[gg-1]
        attacker.atack(defender)
        print(f"{attacker.name} атаковал {defender.name + 'а'}!\nУ {defender.name + 'а'} осталось {defender.hp} здоровья.")

        if defender.hp == 0:
            print(f"{attacker.name} одержал победу в этой битве!")
            break

    else:

        print("Увидимся!!!")
        break