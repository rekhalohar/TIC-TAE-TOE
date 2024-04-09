def printboard(xState, yState):
    zero = 'X' if xState[0] else ('O' if yState[0] else ' ')
    one = 'X' if xState[1] else ('O' if yState[1] else ' ')
    two = 'X' if xState[2] else ('O' if yState[2] else ' ')
    three = 'X' if xState[3] else ('O' if yState[3] else ' ')
    four = 'X' if xState[4] else ('O' if yState[4] else ' ')
    five = 'X' if xState[5] else ('O' if yState[5] else ' ')
    six = 'X' if xState[6] else ('O' if yState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if yState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if yState[8] else ' ')

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def check_winner(xState, yState):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if all(xState[i] == 1 for i in combo) or all(yState[i] == 1 for i in combo):
            return True
    return False

def restart_game():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]

if __name__ == "__main__":
    print("Hello gamers")

    while True:
        xState, yState = restart_game()
        turn = 1

        while True:
            if turn == 1:
                print("X's chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
                printboard(xState, yState)
                if check_winner(xState, yState):
                    print("player1 wins!")
                    break
                turn = 2
            else:
                print("O's chance")
                value = int(input("Please enter a value: "))
                yState[value] = 1
                printboard(xState, yState)
                if check_winner(xState, yState):
                    print("player2 wins!")
                    break
                turn = 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
