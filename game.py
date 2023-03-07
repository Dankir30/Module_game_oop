"""
This module for build and start the game
"""
import game_exceptions
import game_menu
import models
import settings


def play():
    """
    This method for game process. Creatу player and enemy objects , depending on your game mode choice.
    Validate inputs.
    :return: None
    """
    player_name = input('Enter your name, please:\n')
    game_menu.menu(player_name.lower())
    game_mode = input('Choose game mode: normal or hard\n')
    game_menu.menu(game_mode.lower())
    while game_mode.lower() not in settings.GAME_MODE:
        game_mode = input('Wrong!. Be attentive. Choose game mode: normal or hard\n')
    start_game = input('If your want start game, enter !start.\n'
                       'For more commands type !help, please.\n')
    while game_menu.menu(start_game.lower()) != '!start':
        start_game = input('If your want start game, enter !start\n')
    if game_mode == 'normal':
        player = models.Player(player_name, game_mode)
        level = 1
        enemy = models.Enemy(level)
    else:
        player = models.HardPlayer(player_name, game_mode)
        level = 1
        enemy = models.HardEnemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except game_exceptions.EnemyDown:
            if game_mode == 'normal':
                print('-------You won this duel!!!-------- \n')
                level += 1
                player.score += 5
                print(f'Next enemy level: {level}\n')
                enemy = models.Enemy(level)
            else:
                print('-------You won this duel!!!-------- \n')
                level += 1
                player.score += 15
                print(f'Next enemy level: {level}\n')
                enemy = models.HardEnemy(level)


if __name__ == '__main__':
    try:
        play()
    except game_exceptions.GameOver as go:
        go.save_score()
        print('Game over!!!')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!!! ;-)')
