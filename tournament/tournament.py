'''
Take the league matches result and generate table with scores:
MP - matches playes, W - win, D - draw, L - lose, P - points
'''

import operator

league = [
            "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]

def tally(league):
    result = ['{:31}| {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.format('Team', 'MP', ' W', ' D', ' L', 'P'), ]

    if league == None:
        return result

    matches = [x.split(';') for x in league]

    # Set teams and count matches played by each:
    t1 = []
    board = {}

    for match in matches:
        for i in range(0, 2):
            t1.append(match[i])
            board[match[i]] = [t1.count(match[i]), 0, 0, 0, 0]

            # Check the matches result add them into dictionary:
    for match in matches:
        if match[2] == 'win':
            board[match[0]][1] += 1
            board[match[1]][3] += 1
        if match[2] == 'loss':
            board[match[1]][1] += 1
            board[match[0]][3] += 1
        if match[2] == 'draw':
            board[match[1]][2] += 1
            board[match[0]][2] += 1

    # Sum up the points:
    for row in board:
        board[row][4] = (board[row][1] * 3) + board[row][2]

    # Present the league:
    for row in board:
        result.append(
            '{:31}| {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.format(row, board[row][0], board[row][1], board[row][2],
                                                              board[row][3], board[row][4]), )

    final = sorted(sorted(result), key=operator.itemgetter(-1), reverse=True)
    for i in final:
        print(i)
    return final

tally(league)