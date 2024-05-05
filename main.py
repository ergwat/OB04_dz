from abc import ABC, abstractmethod
import random


class Weapon(ABC):

    def __init__(self, max_damage: int):
        self.max_damage = max_damage

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, max_damage: int):
        self.max_damage = max_damage
        self.distance = 1
        self.currentweapon = "Меч"

    def attack(self):
        damage = random.randint(0,self.max_damage+1)
        print(f"Боец бьёт мечом с силой {damage} в ближнем бою")
        return damage

class Bow(Weapon):
    def __init__(self, max_damage: int):
        self.max_damage = max_damage
        self.distance = 20
        self.currentweapon = "Лук"

    def attack(self):
        damage = random.randint(0, self.max_damage + 1)
        print(f"Боец стреляет из лука с силой {damage} пунктов на {self.distance} метров")
        return damage
class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
        print(f"На арену выходит боец. У него в руках {self.weapon.currentweapon}, с потенциальным уроном {self.weapon.max_damage} единиц")

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец изменил оружие на {self.weapon.currentweapon}, с потенциальным уроном {self.weapon.max_damage} единиц")

    def choose_monster(self, monster):
        self.monster = monster
    def attack(self):
        damage = self.weapon.attack()
        self.monster.hp -= damage
        self.monster.check_hp()
        return self.monster.hp
class Monster():
    def __init__ (self, name, hp: int, jump_length):
        self.name = name
        self.hp = hp
        self.jump_length = jump_length
        print (f"На арену выходит монстр {self.name} с {self.hp} hp. Он умеет прыгать на расстояние до {self.jump_length} метров")
    def check_hp(self):
        if self.hp <= 0:
            print(f"{self.name} благополучно помер")
        else:
            print(f"{self.name} Всё ещё жив, у него осталось {self.hp} hp")

#monster1 = Monster("Пятачок",random.randint(10,30), random.randint(1,20))
#warrior1 = Fighter(Sword(random.randint(3,51)))
#warrior1.choose_monster(monster1)

# while monster1.hp > 0:
#     warrior1.attack()
#     warrior1.changeWeapon(Bow(random.randint(1,11)))
