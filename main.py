"""The functions of choosing a character and his skills are described.
Also the calculation of the damage done, the blocking of damage.
Also the calculation of power special skill.
"""
from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Damage calculation."""
    r_damage: int = 0
    if char_class == 'warrior':
        r_damage = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {r_damage} е.д.')
    if char_class == 'mage':
        r_damage = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {r_damage} е.д.')
    if char_class == 'healer':
        r_damage = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {r_damage} е.д.')
    return ''


def defence(char_name: str, char_class: str) -> str:
    """Blocked Damage Calculation."""
    b_damage: int = 0
    if char_class == 'warrior':
        b_damage = 10 + randint(5, 10)
        return f'{char_name} блокировал {b_damage} е.д. урона'
    if char_class == 'mage':
        b_damage = 10 + randint(-2, 2)
        return f'{char_name} блокировал {b_damage} е.д. урона'
    if char_class == 'healer':
        b_damage = 10 + randint(2, 5)
        return f'{char_name} блокировал {b_damage} е.д. урона'
    return ''


def special(char_name: str, char_class: str) -> str:
    """Calculate the power of special skills."""
    s_skills: int = 0
    if char_class == 'warrior':
        s_skills = 80 + 25
        return (f'{char_name} применил специальное умение «Выносливость '
                f'+{s_skills}»')
    if char_class == 'mage':
        s_skills = 5 + 40
        return (f'{char_name} применил специальное умение «Атака +{s_skills}»')
    if char_class == 'healer':
        s_skills = 10 + 30
        return (f'{char_name} применил специальное умение «Защита +{s_skills}»'
                )
    return ''


def start_training(char_name: str, char_class: str) -> str:
    """Сharacter training."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Character selection."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior, Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, чтобы выбрать '
                               'другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
