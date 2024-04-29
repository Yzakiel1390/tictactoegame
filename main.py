class Player:
    X = "X"
    O = "O"

def check_win(game: list) -> bool:
    for i in range(3):
        if (game[i][0] == game[i][1] == game[i][2] != " "):
            return True
        if (game[0][i] == game[1][i] == game[2][i] != " "):
            return True
    if (game[0][0] == game[1][1] == game[2][2] != " "):
        return True
    if (game[0][2] == game[1][1] == game[2][0] != " "):
        return True
    return False

def valid_local(game: list, play: int) -> bool:
    return True if (9 > play >= 0 and game[play // 3][play % 3] == " ") else False

def printgame(game: list):
    for row in game:
        print(f" | ".join(row))
        print("-" * 9)

def main():
    game = [[" " for _ in range(3)] for _ in range(3)]
    player = input("Jogador 1 [O ou X]: ")
    while player != Player.O and player != Player.X:
        player = input("Jogador 1 [O ou X]: ")
    
    for _ in range(9):
        printgame(game)

        play = int(input("- Digite um Local (1-9): ")) - 1
        while not valid_local(game, play):
            print("Local inválido, digite outro.")
            play = int(input("- Digite um Local (1-9): ")) - 1
        
        game[play // 3][play % 3] = player
        if (check_win(game)):
            printgame(game)
            print(f" - Jogo Finalizado! \n - O Vencendor foi: {player}")
            break
        else:
            player = Player.O if player == Player.X else Player.X
    else:
        printgame(game)
        print(" - Empate!")

if (__name__ == "__main__"):
    main()