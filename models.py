"""
This Module for Player and Enemy classes
"""
import random

import game_exceptions
import game_menu
import settings


class Enemy:
    """
    This class describes behavior Enemy object
    """
    def __init__(self, level):
        """
        Initialization
        :param level: level = enemy_lives
        """
        self.level = level
        self.enemy_lives = level

    @staticmethod
    def select_attack():
        """
         random enemy attack
        :return: random int digit from list
        """

        return random.choice([1, 2, 3])

    def decrease_lives(self):
        """
         Decreasing enemy`s live -1 ,  when it`s = 0 calling exception
        :return: None
        """
        self.enemy_lives -= 1
        if self.enemy_lives == 0:
            raise game_exceptions.EnemyDown


class Player:
    """
       This class describes behavior Player object

    """
    def __init__(self, name, game_mode):
        """
        Initialization
        :param name: the name entered by the player
        :param game_mode:  difficulty level  picked by player
        """
        self.name = name
        self.player_lives = settings.PLAYER_LIVES
        self.score = settings.DEFAULT_SCORE
        self.allowed_attacks = ['1', '2', '3']
        self.game_mode = game_mode

    @staticmethod
    def fight(attack, defense):
        """
        This method return 1 , -1 , or 0  depending on the chosen attack and defense
        :param attack: chosen by player 1, 2 or 3
        :param defense: random choice from list [1,2,3]
        :return: 1 , -1 or 0
        """
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or \
                (attack == 3 and defense == 1):
            return 1
        if attack == defense:
            return 0
        return -1

    def decrease_lives(self):
        """
        Decreasing player live -1 ,  when it`s = 0 calling exception
        :return: None
        """
        self.player_lives -= 1
        if self.player_lives == 0:
            print(f'Unfortunately, you are dead\n'
                  f'Final score: {self.score}')
            raise game_exceptions.GameOver(self.score, self.name, self.game_mode)

    def attack(self, enemy_obj):
        """
        printing result of fight depending on player`s and enemy`s choice. When wins player,
        his score increase +1 and decrease enemy live -1
        :param enemy_obj: Enemy class object
        :return: None
        """
        my_attack_row = input('Now, YOU have to attack your opponent.\n'
                'Choose your attack (by number): (1) Wizard,  (2) Warrior, (3) Robber\n')

        while game_menu.menu(my_attack_row.lower()) not in self.allowed_attacks:
            my_attack_row = input('Choose your attack (by number):'
                                  '(1) Wizard,  (2) Warrior, (3) Robber\n')
        else:
            my_attack = int(my_attack_row)
            enemy_attack = enemy_obj.select_attack()
            result_fight = self.fight(my_attack, enemy_attack)
            if result_fight == 1:
                self.score += 1
                enemy_obj.decrease_lives()
                print(f'Your choice: {my_attack}, Enemy`s choice: {enemy_attack}\n'
                      f'-----------You attacked successfully!-------------\n'
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            elif result_fight == -1:
                print(f'Your choice is {my_attack}, enemy`s choice is {enemy_attack}\n'
                      f"----------You missed!----------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            else:
                print(f'Your choice is {my_attack}, enemy`s choice is {enemy_attack}\n'
                      f"-----------It's a draw!-------------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')

    def defence(self, enemy_obj):
        """
        printing result of fight depending on player`s and enemy`s choice. When wins enemy,
        decrease player live -1
        :param enemy_obj: Enemy class Object
        :return: NOne
        """
        my_attack_row = input('Now, YOU have to DEFEND.\n'
                              'Pick (by number): (1) Wizard,  (2) Warrior, (3) Robber\n')
        while game_menu.menu(my_attack_row.lower()) not in self.allowed_attacks:
            my_attack_row = input('Pick (by number): (1) Wizard,  (2) Warrior, (3) Robber\n')
        else:
            my_attack = int(my_attack_row)
            enemy_attack = enemy_obj.select_attack()
            result_fight = self.fight(enemy_attack, my_attack)

            if result_fight == 1:
                self.decrease_lives()
                print(f'Your choice: {my_attack}, enemy`s choice: {enemy_attack}\n'
                      f'-------------You missed-------------\n'
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            elif result_fight == -1:
                print(f'Your choice: {my_attack}, enemy`s choice: {enemy_attack}\n'
                      f"-------------You successfully defended!--------------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            else:
                print(f'Your choice: {my_attack}, enemy`s choice: {enemy_attack}\n'
                      f"----------It's a draw!-----------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')


class HardPlayer(Player):
    """
    It`s player class for hard game mode
    """
    def attack(self, enemy_obj):
        """

       printing result of fight depending on player`s and enemy`s choice. When wins player,
       his score increase + setting.HARD_MODE_MULTIPLIER and decrease enemy live -1
       :param enemy_obj: Enemy class object
       :return: None
       """

        my_attack_row = input('Now, YOU have to attack your opponent.\n'
                'Choose your attack (by number): (1) Wizard,  (2) Warrior, (3) Robber\n')

        while game_menu.menu(my_attack_row.lower()) not in self.allowed_attacks:
            my_attack_row = input('Choose your attack (by number):'
                                  '(1) Wizard,  (2) Warrior, (3) Robber\n')
        else:
            my_attack = int(my_attack_row)
            enemy_attack = enemy_obj.select_attack()
            result_fight = self.fight(my_attack, enemy_attack)
            if result_fight == 1:
                self.score += settings.HARD_MODE_MULTIPLIER
                enemy_obj.decrease_lives()
                print(f'Your choice: {my_attack}, Enemy`s choice: {enemy_attack}\n'
                      f'-----------You attacked successfully!-------------\n'
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            elif result_fight == -1:
                print(f'Your choice is {my_attack}, enemy`s choice is {enemy_attack}\n'
                      f"----------You missed!----------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')
            else:
                print(f'Your choice is {my_attack}, enemy`s choice is {enemy_attack}\n'
                      f"-----------It's a draw!-------------\n"
                      f'Score in this round:{self.score}\n'
                      f'Your lives are {self.player_lives}\n'
                      f'Enemy lives are {enemy_obj.enemy_lives}\n')


class HardEnemy(Enemy):
    """
    This class for emeny with hard game mode
    """
    def __init__(self, level):
        """
        Initialization
        :param level: level = enemy_lives * HARD_MODE_MULTIPLIER
        """
        super().__init__(level)
        self.enemy_lives = settings.HARD_MODE_MULTIPLIER * level
