"""
This module contains game menu
"""
import settings


def menu(choice):
    """
    Validate and return choice depending on what your choice is
    :param choice: your input from module game.py
    :return: choice
    """
    if choice == '!exit':
        raise SystemExit
    if choice == '!start':
        return choice
    if choice == '!help':
        print(f'Commands, that you can use: {settings.COMMANDS}')
        return choice
    if choice == '!show_scores':
        with open(settings.FILE_PATH, encoding='utf-8') as file:
            for line in file:
                print(line)
        return choice
    return choice
