import user_diff as ud
import cm_pattern as cmp
import cb_guess as cbg
import feedback as fb
import time

color_list_options = ['RED', 'YELLOW', 'BLUE', 'GREEN', 'PINK', 'PURPLE']
level_rounds_diff = { 'easy': 12, 'medium': 8, 'hard': 4}


def game():
    print('Welcome to the MASTERMIND game, please enjoy and follow the instructions, GOOD LUCK!!\n')
    time.sleep(1)
    ROUNDS_TO_PLAY = ud.ask_user_difficulty_level(dict=level_rounds_diff)

    print(f'\n You will play {ROUNDS_TO_PLAY} rounds \n ')
    print('--------------------------------------------------------------')

    CODEMAKER_PATTERN = cmp.codemaker_code_pattern(lst_color=color_list_options)
    rounds_played = 1

    while rounds_played <= ROUNDS_TO_PLAY:

        code_breaker_guess = cbg.codebreaker_guess(lst_color=color_list_options)
        print('\nYour guess is:')
        print(code_breaker_guess)

        rounds_played += 1

        feedback_list = fb.feedback_codemaker(CODEMAKER_PATTERN, code_breaker_guess)
        print('\nYour feed back is: \n')
        print(feedback_list)

        print(f'\nThis was the round {rounds_played - 1} \n')
        print('-------------------------------------------------------')

        if CODEMAKER_PATTERN == code_breaker_guess:
            print('You won!!!!!!')
            break

    if rounds_played > ROUNDS_TO_PLAY:
        print("You loose, you run out of rounds!!!! Try another time")
        print(f" \nThe codemaker pattern was {CODEMAKER_PATTERN}")

print(game())