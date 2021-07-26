from os import system

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sign = 0
 
def display_board(board):
    print("+---+---+---+")
    print("|", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("+---+---+---+")
    print("|", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("+---+---+---+")
    print("|", board[2][0], "|", board[2][1], "|", board[2][2], "|")
    print("+---+---+---+")

def make_list_of_free_fields(board):
    global temp
    temp = []
    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if "X" != board[i][j] and "O" != board[i][j]:
                temp.append(board[i][j])
            
    if temp == []:
        print("EMPATE!")
        return GO()


def enter_move(board):
    system("cls")
    make_list_of_free_fields(board)
    display_board(board)
    
    move = False
    
    while move == False:
        try:
            m = int(input("Escolha a sua casa: "))
        
            if m < 1 or m > 9:
                print("Número inválido. Escolha entre 1 e 9.")
                move = False

            elif m not in temp:
                print("Casa ocupada. Tente outra.")
                move = False

            else:
                move = True

        except ValueError:    
            print("Entrada inválida. Use apenas números.")
            move = False
    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if m == board[i][j]:
                board[i][j] = "O"
                victory_for(board, sign)
    draw_move(board)

def victory_for(board, sign):
    system('cls')
    i = 0
        
    #Check rows
    for i in range(0, len(board[i])):
        if board[i] == ["X", "X", "X"]:
            sign = "Você perdeu..."
            print(sign)
            return GO()

        if board[i] == ["O", "O", "O"]:
            sign = "Você venceu!"
            print(sign)
            return GO()
            
    #Check colums
    col = []
    count = 0
    cc = [count]
    i = 0
    j = 0

    while count != len(board[j]):
        for i in range(0, len(board[i])):
            for j in cc:
                col.append(board[i][j])
                if col == ["X", "X", "X"]:
                    sign = "Você perdeu..."
                    print(sign)
                    return GO()
        
                if col == ["O", "O", "O"]:
                    sign = "Você venceu!"
                    print(sign)
                    return GO()
                
        col = []
        cc.pop()
        count += 1
        cc.append(count)
        
    #Check diags
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    
    if diag1 == ["X", "X", "X"] or diag2 == ["X", "X", "X"]:
        sign = "Você perdeu..."
        print(sign)
        return GO()

    if diag1 == ["O", "O", "O"] or diag2 == ["O", "O", "O"]:
        sign = "Você venceu!"
        print(sign)
        return GO()
        

def draw_move(board):
    make_list_of_free_fields(board)
    from random import choice

    nove = False
    
    while nove == False:
        n = choice(temp)
        
        if n < 1 or n > 9:
            nove = False
        
        elif n not in temp:
            nove = False

        else:
            nove = True

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if n == board[i][j]:
                board[i][j] = "X"
                victory_for(board, sign)
    enter_move(board)

def GO():
    display_board(board)
    exit()

enter_move(board)
