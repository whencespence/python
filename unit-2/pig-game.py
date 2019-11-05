import random
player_one_total = 0
player_two_total = 0
turn = 1
MAX_SCORE = 20
while True:
    choice = input('Player{} Roll or Hold [r/h]'.format(turn))
    val = random.randint(1, 6)
    if choice == 'r':
        print('Player{} rolls {}'.format(turn, val))
        if val != 1:
            if turn  == 1:
                player_one_total += val
            else:
                player_two_total += val
        
        else:
            print('Player{} loses turn'.format(turn))
            if turn == 1:
                player_one_total = 0
                turn = 2
            else:
                player_two_total = 0
                turn = 1
    else:
        print('Player{} holds '.format(turn))
        if turn == 1:
            turn = 2
        else:
            turn = 1
    
    #check if someone wins the game
    if player_one_total >= MAX_SCORE or player_two_total >= MAX_SCORE:
        break
if player_one_total >= MAX_SCORE:
    print('PLAYER1 WINS')
else:
    print('PLAYER2 WINS')