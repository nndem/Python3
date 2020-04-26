"""
Есть класс "Воин". От него создаются два экземпляра-юнита.
Каждому устанавливается здоровье в 100 очков.
В случайном порядке они бьют друг друга.
Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

"""
import random


class Unit:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20
    
    def kick(self, enemy):
        print(self.name, 'атаковал')
        self.get_injure(enemy)

    def get_injure(self, enemy):
        enemy.health -= self.damage  # подразумевается, что у enemy будет свойство health
        self.check_health(enemy)
        print(f'У {enemy.name} осталось {enemy.health}')

    def check_health(self, enemy):
        if enemy.health == 0:
            self.dead(enemy)

    def dead(self, enemy):
        print(f'{enemy.name} is dead')
        return

def main():
    sergey = Unit('Sergey Lazarev')
    dima = Unit('Dima Bilan')
    while sergey.health > 0 and dima.health > 0:
        sergey.kick(dima) if random.randint(0, 1) else dima.kick(sergey)

if __name__ == '__main__':
    main()



