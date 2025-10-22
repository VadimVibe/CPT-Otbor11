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

place,hod_pl,hod, hod_zn = [' ']*10,['первый','второй','третий','четвертый','пятый'], 0, ['О','X']
name = ['Игрок 1','Игрок 2']

def play(hod):
    while hod != 10:
        if hod == 0:
            print('Добро пожаловать в игру! Уважаемые игроки, введите свои имена в систему через пробел, иначе просто нажмите клавишу Enter')
            names = str(input()).split(' ')
            if names[0] != '':
                name[0],name[1] = names[1],names[0]
            print(f'Уважаемые {name[1]} и {name[0]}, перед тем, как придступить к игре, хотелось бы вам напомнить правила:')
            print(print_play_game())
        else:
            print(f'{name[0]}, делайте свой {hod_pl[int((hod - 1)%2)]} ход!  Укажите номер ячейки, в которую вы поставите {hod_zn[hod%2]}')
            place[int(input())] = hod_zn[int(hod%2)]
            print_place()
            if if_win() == 1:
                print(f'{name[hod%2]}, поздравляю, вы победили!')
                break

        hod += 1