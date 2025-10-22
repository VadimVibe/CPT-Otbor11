def print_place():
    print(place[1], '|', place[2], '|', place[3])
    print('--+---+--')
    print(place[4], '|', place[5], '|', place[6])
    print('--+---+--')
    print(place[7], '|', place[8], '|', place[9])

def print_play_game():
    print("Игровое поле с номерами ячеек")
    print(' 1 | 2 | 3 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 7 | 8 | 9 ')

def if_win():
    for i in range(0,7,3):
        if place[1+i] == place[2+i] == place[3+i] and place[1+i] != ' ': return 1
    for i in range(0,3):
        if place[1+i] == place[4+i] == place[7+i] and place[1+i] != ' ': return 1
    if (place[1] == place[5] == place[9] and place[1] != ' ') or (place[3] == place[5] == place[7] and place[3] != ' '): return 1
    return  0