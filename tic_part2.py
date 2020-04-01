# winner_is_2 = [[2, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# winner_is_1 = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# winner_is_also_1 = [[0, 1, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
#
# no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 2]]
#
# also_no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 0]]
#
# winner_row0=[[2, 0, 0],
# 	[1, 0, 2],
# 	[0, 0, 2]]


def game_winner(game):

    def is_row(game):
        for i in range(3):
            if(len(set(game[i]))==1 and game[i][0] != 0):
                print('row {} win'.format(i))
                return game[i][0]
        return 0

    def is_col(game):
        for i in range(3):
            if(len(set(row[i] for row in game))==1 and game[0][i] != 0):
                print('column {} win'.format(i))
                return game[0][i]
        return 0

    def is_diag(game):
        y = [row[i] for row in game for i in range(3)]
        # print(y)
        # print(set(y[i] for i in (0, 4, 8)))
        # print(set(y[i] for i in (2, 4, 6)))
        if len(set(y[i] for i in (0, 4, 8)))==1 and game[0][0]!= 0:
            print('diag 1 win')
            return game[0][0]
        if len(set(y[i] for i in (2, 4, 6)))==1 and game[0][2]!= 0:
            print('diag 2 win')
            return game[0][2]
        return 0

    for func in (is_row, is_col, is_diag):
        result=func(game)
        if result:
            return result

    # result=is_row(game)
    # if result:
    #     return result
    # result=is_col(game)
    # if result:
    #     return result
    # result=is_diag(game)
    # if result:
    #     return result

    return 0

# all=[winner_is_2, winner_is_1, winner_is_also_1, no_winner, also_no_winner]
#
#
#
# for res in all:
#     print (res)
#     result=game_winner(res)
#     if result:
#         print('The winner is player {}'.format(result))
#     else:
#         print ('No winner')