# ============================================================
# TERMINAL TIC-TAC-TOE
# A clean text-based board game using Python 3
# Single source code file - no external libraries required
# ============================================================

import random
import os
import time


# ------------------------------------------------------------
# CLEAR TERMINAL SCREEN
# ------------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------------------------
# PAUSE
# ------------------------------------------------------------
def pause():
    input("\nPress ENTER to continue...")


# ------------------------------------------------------------
# DISPLAY TITLE
# ------------------------------------------------------------
def display_title():
    print("=" * 55)
    print("              TERMINAL TIC-TAC-TOE")
    print("=" * 55)


# ------------------------------------------------------------
# DISPLAY MAIN MENU
# ------------------------------------------------------------
def display_menu():
    clear_screen()
    display_title()

    print("\nMAIN MENU")
    print("-" * 55)
    print("1. Player vs Computer")
    print("2. Player vs Player")
    print("3. View Score")
    print("4. Reset Score")
    print("5. Exit")
    print("-" * 55)


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------
def display_board(board):
    print("\n")
    print("              TIC-TAC-TOE BOARD")
    print()

    print("                  |     |")
    print(f"               {board[0]}  |  {board[1]}  |  {board[2]}")
    print("             ------+-----+------")
    print("                  |     |")
    print(f"               {board[3]}  |  {board[4]}  |  {board[5]}")
    print("             ------+-----+------")
    print("                  |     |")
    print(f"               {board[6]}  |  {board[7]}  |  {board[8]}")
    print("                  |     |")
    print()


# ------------------------------------------------------------
# DISPLAY POSITION GUIDE
# ------------------------------------------------------------
def display_position_guide():
    print("POSITION GUIDE")
    print()
    print("                  1  |  2  |  3")
    print("                -----+-----+-----")
    print("                  4  |  5  |  6")
    print("                -----+-----+-----")
    print("                  7  |  8  |  9")
    print()


# ------------------------------------------------------------
# CHECK WINNER
# ------------------------------------------------------------
def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


# ------------------------------------------------------------
# CHECK DRAW
# ------------------------------------------------------------
def check_draw(board):
    for cell in board:
        if cell not in ["X", "O"]:
            return False

    return True


# ------------------------------------------------------------
# GET PLAYER MOVE
# ------------------------------------------------------------
def get_player_move(board, player_name, symbol):
    while True:
        try:
            choice = input(
                f"{player_name} ({symbol}), choose a position (1-9): "
            ).strip()

            if choice.lower() == "q":
                return -1

            position = int(choice)

            if position < 1 or position > 9:
                print("Invalid choice! Enter a number from 1 to 9.")
                continue

            index = position - 1

            if board[index] in ["X", "O"]:
                print("That position is already occupied. Try again.")
                continue

            return index

        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")


# ------------------------------------------------------------
# COMPUTER MOVE - SMART AI
# ------------------------------------------------------------
def computer_move(board):
    # 1. Try to win
    for i in range(9):
        if board[i] not in ["X", "O"]:
            test_board = board.copy()
            test_board[i] = "O"

            if check_winner(test_board, "O"):
                return i

    # 2. Block player's winning move
    for i in range(9):
        if board[i] not in ["X", "O"]:
            test_board = board.copy()
            test_board[i] = "X"

            if check_winner(test_board, "X"):
                return i

    # 3. Take center
    if board[4] not in ["X", "O"]:
        return 4

    # 4. Take a corner
    corners = [0, 2, 6, 8]
    available_corners = [
        i for i in corners if board[i] not in ["X", "O"]
    ]

    if available_corners:
        return random.choice(available_corners)

    # 5. Take any available position
    available_positions = [
        i for i in range(9) if board[i] not in ["X", "O"]
    ]

    if available_positions:
        return random.choice(available_positions)

    return -1


# ------------------------------------------------------------
# PLAY PLAYER VS COMPUTER
# ------------------------------------------------------------
def player_vs_computer(scores):
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    clear_screen()
    display_title()

    print("\nPLAYER VS COMPUTER")
    print("-" * 55)
    print("You are X")
    print("Computer is O")
    print("Enter Q at any time to return to the main menu.")
    print()

    display_position_guide()

    while True:
        # PLAYER TURN
        clear_screen()
        display_title()
        print("\nPLAYER VS COMPUTER")
        display_board(board)

        move = get_player_move(board, "Player", "X")

        if move == -1:
            return

        board[move] = "X"

        if check_winner(board, "X"):
            clear_screen()
            display_title()
            display_board(board)

            print("🎉 CONGRATULATIONS!")
            print("You defeated the computer!")

            scores["Player"] += 1

            pause()
            break

        if check_draw(board):
            clear_screen()
            display_title()
            display_board(board)

            print("🤝 GAME DRAW!")
            scores["Draws"] += 1

            pause()
            break

        # COMPUTER TURN
        clear_screen()
        display_title()
        print("\nPLAYER VS COMPUTER")
        display_board(board)

        print("Computer is thinking...")
        time.sleep(0.7)

        move = computer_move(board)

        if move != -1:
            board[move] = "O"

        if check_winner(board, "O"):
            clear_screen()
            display_title()
            display_board(board)

            print("💻 COMPUTER WINS!")
            print("Better luck next time.")

            scores["Computer"] += 1

            pause()
            break

        if check_draw(board):
            clear_screen()
            display_title()
            display_board(board)

            print("🤝 GAME DRAW!")
            scores["Draws"] += 1

            pause()
            break


# ------------------------------------------------------------
# PLAY PLAYER VS PLAYER
# ------------------------------------------------------------
def player_vs_player(scores):
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    clear_screen()
    display_title()

    print("\nPLAYER VS PLAYER")
    print("-" * 55)

    player1 = input("Enter Player 1 name: ").strip()

    if not player1:
        player1 = "Player 1"

    player2 = input("Enter Player 2 name: ").strip()

    if not player2:
        player2 = "Player 2"

    current_player = player1
    current_symbol = "X"

    while True:
        clear_screen()
        display_title()

        print(f"\n{player1} = X")
        print(f"{player2} = O")

        display_board(board)

        move = get_player_move(
            board,
            current_player,
            current_symbol
        )

        if move == -1:
            return

        board[move] = current_symbol

        if check_winner(board, current_symbol):
            clear_screen()
            display_title()
            display_board(board)

            print(f"🎉 {current_player} WINS!")
            print("Congratulations!")

            if current_symbol == "X":
                scores["Player 1"] += 1
            else:
                scores["Player 2"] += 1

            pause()
            break

        if check_draw(board):
            clear_screen()
            display_title()
            display_board(board)

            print("🤝 GAME DRAW!")

            scores["Draws"] += 1

            pause()
            break

        # Change player
        if current_symbol == "X":
            current_player = player2
            current_symbol = "O"
        else:
            current_player = player1
            current_symbol = "X"


# ------------------------------------------------------------
# SHOW SCORE
# ------------------------------------------------------------
def show_score(scores):
    clear_screen()
    display_title()

    print("\n🏆 SCOREBOARD")
    print("-" * 55)

    print(f"Player Wins     : {scores['Player']}")
    print(f"Computer Wins   : {scores['Computer']}")
    print(f"Player 1 Wins   : {scores['Player 1']}")
    print(f"Player 2 Wins   : {scores['Player 2']}")
    print(f"Draws           : {scores['Draws']}")

    print("-" * 55)

    total_games = (
        scores["Player"]
        + scores["Computer"]
        + scores["Player 1"]
        + scores["Player 2"]
        + scores["Draws"]
    )

    print(f"Total Games     : {total_games}")

    pause()


# ------------------------------------------------------------
# RESET SCORE
# ------------------------------------------------------------
def reset_score(scores):
    clear_screen()
    display_title()

    print("\nRESET SCORE")
    print("-" * 55)

    confirmation = input(
        "Are you sure you want to reset all scores? (Y/N): "
    ).strip().lower()

    if confirmation == "y":
        for key in scores:
            scores[key] = 0

        print("\nAll scores have been reset successfully!")
    else:
        print("\nReset cancelled.")

    pause()


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
def main():
    scores = {
        "Player": 0,
        "Computer": 0,
        "Player 1": 0,
        "Player 2": 0,
        "Draws": 0
    }

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            player_vs_computer(scores)

        elif choice == "2":
            player_vs_player(scores)

        elif choice == "3":
            show_score(scores)

        elif choice == "4":
            reset_score(scores)

        elif choice == "5":
            clear_screen()
            display_title()

            print("\nThank you for playing!")
            print("Goodbye! 👋")
            print()

            break

        else:
            print("\nInvalid option!")
            print("Please select a number from 1 to 5.")
            time.sleep(1.5)


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------
if __name__ == "__main__":
    main()