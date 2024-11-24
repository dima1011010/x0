

board = list(range(1,10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def take_input(token):
    valid = False
    while not valid:
        answer = input("куда поставить  " + token + "?")
        try:
            answer = int(answer)
        except:
            print("error")
            continue
        if answer >= 1 & answer <= 9:
            if(str(board[answer -1]) not in "XO"):
                board[answer -1] = token
                valid = True
            else:
                print("место занято")
        else:
            print("введите число от 1 до 9")

def check_win (board):
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for each in win_line:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main (board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "you win")
                win = True
                break
            if counter == 9:
                print("dead heat")
                break
    draw_board(board)
main(board)