"""
This module for custom game exceptions
"""
import settings


class GameOver(Exception):
    """
    ---It`s another  method to write info into file(just simple writing in the file)---

    def __init__(self, final_score, name):
        self.final_score = str(final_score)
        self.name = str(name)
        self.recorded = self.save_score()

    def save_score(self):
        with open(settings.FILE_PATH, 'a+') as fp:
            fp.write(f'Name: {self.name}   Score: {self.final_score}\n')
    """

    def __init__(self, final_score, name, game_mode):
        """
        Initialization
        :param final_score:
        :param name:
        :param game_mode:
        """
        self.final_score = str(final_score)
        self.name = str(name)
        self.game_mode = game_mode

    def save_score(self):
        """
        This method save top 10 best scores
        :return: None
        """
        with open(settings.FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(f'Name:{self.name} Score:{self.final_score} Mode:{self.game_mode}\n')

        with open(f'{settings.FILE_PATH}', encoding='utf-8') as file:
            scores_list = file.readlines()
            row_list = [list(x.rstrip('\n').split()) for x in scores_list]
            unsorted_data = {}
            for lst in row_list:
                unsorted_data[int(lst[1].split(':')[1])] = [lst[0].split(':')[1], lst[2].split(':')[1]]
        unsorted_keys = list(unsorted_data.keys())
        sorted_keys = sorted(unsorted_keys)
        sorted_keys.reverse()
        sorted_dict = {i: unsorted_data[i] for i in sorted_keys[:10]}

        with open(f'{settings.FILE_PATH}', 'w+', encoding='utf-8') as file:
            for key, value in sorted_dict.items():
                file.write(f'Name:{value[0]} Score:{key} Mode:{value[1]}\n')


class EnemyDown(Exception):

    """
    This exception for enemy death
    """
