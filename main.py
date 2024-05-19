class Player:
    X, O = "X", "O"

def check_win(board: list) -> bool:
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != " "):
            return True
        if (board[0][i] == board[1][i] == board[2][i] != " "):
            return True
    if (board[0][0] == board[1][1] == board[2][2] != " "):
        return True
    if (board[0][2] == board[1][1] == board[2][0] != " "):
        return True
    return False

def valid_local(board: list, play: int) -> bool:
    return 9 > play >= 0 and board[play // 3][play % 3] == " "

def printgame(board: list):
    for row in board:
        print(f"\033[30m{" | ".join(row)}\033[m")
        print(f"\033[30m{"-" * 9}\033[m")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = input("\033[33mJogador 1 [O ou X]: \033[m\033[32m").upper()
    while player != Player.O and player != Player.X:
        player = input("\033[33mJogador 1 [O ou X]: \033[m\033[32m").upper()
    
    for _ in range(9):
        printgame(board)

        play = int(input("\033[34m- Digite um Local \033[m\033[31m(1-9)\033[m\033[34m: \033[m\033[32m")) - 1
        while not valid_local(board, play):
            print("\033[31mLocal inválido, digite outro.\033[m")
            play = int(input("\033[34m- Digite um Local \033[m\033[31m(1-9)\033[m\033[34m: \033[m\033[32m")) - 1
        
        board[play // 3][play % 3] = player
        if check_win(board):
            printgame(board)
            print(f"\033[36m - Jogo Finalizado! \033[m\n\033[32m - O Vencendor foi: \033[m\033[33m{player}\033[m")
            break
        player = Player.O if player == Player.X else Player.X
    else:
        printgame(board)
        print("\033[30m - Empate!\033[m")

if __name__ == "__main__":
    main()