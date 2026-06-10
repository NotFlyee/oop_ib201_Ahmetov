class Weapon:
    def __init__(self, name: str, damage: float, range: float):
        self.__name = name
        self.__damage = damage
        self.__range = range
    
    def hit(self, actor: 'BaseCharacter', target: 'BaseCharacter') -> str | None:
        if not target.is_alive():
            print('Враг уже повержен')
            return
        
        actor_pos_x, actor_pos_y = actor.get_coords()
        target_pos_x, target_pos_y = target.get_coords()
        distance = ((target_pos_x - actor_pos_x) ** 2 + (target_pos_y - actor_pos_y) ** 2) ** 0.5
        if distance > self.__range:
            print(f'Враг слишком далеко для оружия {self.__name}')
            return
        
        target.get_damage(self.__damage)
        print(f'Врагу нанесен урон оружием {self.__name} в размере {self.__damage}')

    def __str__(self):
        return self.__name
    
class BaseCharacter:
    def __init__(self, pos_x: float, pos_y: float, hp: float):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self._hp = hp

    def move(self, delta_x: float, delta_y: float) -> None:
        self.__pos_x += delta_x
        self.__pos_y += delta_y

    def is_alive(self) -> bool:
        return self._hp > 0
    
    def get_damage(self, amount: float) -> None:
        self._hp -= amount

    def get_coords(self) -> tuple[float]:
        return (self.__pos_x, self.__pos_y)
    
class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x: float, pos_y: float, weapon: Weapon, hp: float, ):
        super().__init__(pos_x, pos_y, hp)
        self.__weapon = weapon

    def hit(self, target: BaseCharacter) -> str | None:
        if not isinstance(target, MainHero):
            print('Могу ударить только Главного героя')
            return
        self.__weapon.hit(self, target)
    
    def __str__(self):
        return f'Враг на позиции {self.get_coords()} с оружием {self.__weapon}'
        
class MainHero(BaseCharacter):
    def __init__(self, pos_x: float, pos_y: float, name: str, hp: float):
        super().__init__(pos_x, pos_y, hp)
        self.__name = name
        self.__weapons: list[Weapon] = []

    def hit(self, target: BaseCharacter) -> str | None:
        if not self.__weapons:
            print('Я безоружен')
            return
        if not isinstance(target, BaseEnemy):
            print('Могу ударить только врага')
            return
        active_weapon = self.__weapons[0]
        active_weapon.hit(self, target)

    def add_weapon(self, weapon: Weapon) -> str | None:
        if not isinstance(weapon, Weapon):
            print('Это не оружие')
            return
        self.__weapons.append(weapon)
        print(f'Подобрал {weapon}')
        
    def next_weapon(self) -> str | None:
        if not self.__weapons:
            print('Я безоружен')
            return
        if len(self.__weapons) == 1:
            print('У меня только одно оружие')
            return
        self.__weapons.append(self.__weapons.pop(0))
        print(f'Сменил оружие на {self.__weapons[0]}')
        
    def heal(self, amount: float) -> None:
        max_hp = 200
        self._hp += amount
        if self._hp > max_hp:
            self._hp = max_hp
        print(f'Полечился, теперь здоровья {self._hp}')
