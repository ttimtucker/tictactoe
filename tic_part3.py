from tictactoe.tic_part2 import game_winner

def alternate():
    while True:
        yield 1
        yield 2

def is_legal(game,row,col):
    return not game[row][col]

def update(player, row, col, game):
    game[row][col]=player
    draw(game)
    return game

def draw(game):
    #print(game)
    def cell_dash():
        print(' ---'*3)

    def cell_pipe(move):
        print('| {} '.format(move),end='')

    for row in range(3):
        cell_dash()
        for col in range(3):
            cell_pipe(game[row][col])
        cell_pipe('')
        print()
    cell_dash()
    return 0




game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

player=alternate()
winner=0

while not winner:

    current_player=player.__next__()
    #print('Current player is {}'.format(current_player))

    valid_range=False
    while not valid_range:
        row,col=input('Player {}, enter row,col position for your move: '.format(current_player)).split(',')
        xrow=int(row)-1
        xcol=int(col)-1
        if xrow<0 or xrow>2 or xcol<0 or xrow>2:
            print('Move is out of range.  Try again')
            continue
        valid_range=True

    if is_legal(game,xrow,xcol):
        #print('Legal to move to position {},{}'.format(xrow,xcol))
        game=update(current_player,xrow,xcol,game)
        result = game_winner(game)
        if result:
            print('The winner is player {}.  Ending game'.format(current_player))
            break
    else:
        print('Not Legal to move to position {},{}'.format(xrow,xcol))

