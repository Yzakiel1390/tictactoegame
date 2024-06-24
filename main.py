class Player:
    X, O = "X", "O"

def check_win(board: list[list[str]]) -> bool:
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

def valid_local(board: list[list[str]], play: int) -> bool:
    return 9 > play >= 0 and board[play // 3][play % 3] == " "

def printgame(board: list[list[str]]):
    for row in board:
        print(f"\033[30m{" | ".join(row)}\033[m")
        print(f"\033[30m{"-" * 9}\033[m")

def main():
    board: list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]
    player: str = input("\033[33mPlayer 1 [O or X]: \033[m\033[32m").upper()
    while not player in [Player.O, Player.X]:
        player = input("\033[33mPlayer 1 [O or X]: \033[m\033[32m").upper()
    
    for _ in range(9):
        printgame(board)

        play: int = int(input("\033[34m- Select a location \033[m\033[31m(1-9)\033[m\033[34m: \033[m\033[32m")) - 1
        while not valid_local(board, play):
            print("\033[31mInvalid location, select another.\033[m")
            play = int(input("\033[34m- Select a location \033[m\033[31m(1-9)\033[m\033[34m: \033[m\033[32m")) - 1
        
        board[play // 3][play % 3] = player
        if check_win(board):
            printgame(board)
            print(f"\033[36m - Game Finished! \033[m\n\033[32m - The Winnes was: \033[m\033[33m{player}\033[m")
            break
        player = Player.O if player == Player.X else Player.X
    else:
        printgame(board)
        print("\033[30m - It's a tie!\033[m")

if __name__ == "__main__":
    main()