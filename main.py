# ==========================================================
# PROJECT: Rock Paper Scissors Game
# DESCRIPTION: A terminal-based Rock Paper Scissors game
#              with 3 game modes in Python.
# ==========================================================

import random


def display_welcome():
    """Displays the welcome message and game rules."""
    print("==========================================================")
    print("             WELCOME TO ROCK PAPER SCISSORS")
    print("==========================================================")
    print("Rules   : Rock beats Scissors | Paper beats Rock | Scissors beats Paper")
    print("Controls: Type 'rock' (or 'r'), 'paper' (or 'p'), 'scissors' (or 's').")
    print("          Type 'quit' (or 'q') at any time to exit the game.")
    print("----------------------------------------------------------")


def select_game_mode():
    """Asks the player to choose a game mode and returns '1', '2', or '3'."""
    print("\nSelect a Game Mode:")
    print("  1. First to 3 Wins (First to reach 3 points wins the match)")
    print("  2. 5-Round Match   (Play exactly 5 rounds)")
    print("  3. Free Play       (Play endlessly until you type 'quit')")

    while True:
        mode = input("\nEnter mode number (1, 2, or 3): ").strip()
        if mode in ["1", "2", "3"]:
            return mode
        print("Invalid choice! Please enter 1, 2, or 3.")


def get_computer_choice():
    """Randomly selects and returns 'rock', 'paper', or 'scissors'."""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)


def decide_winner(player_choice, computer_choice):
    """
    Compares choices and returns the result of the round:
    'draw', 'player', or 'computer'.
    """
    if player_choice == computer_choice:
        return "draw"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "player"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player"
    else:
        return "computer"


def display_scoreboard(player_score, computer_score, draws):
    """Displays the current score after each round."""
    print("----------------------------------------------------------")
    print(
        f"SCOREBOARD -> Player: {player_score} | Computer: {computer_score} | Draws: {draws}"
    )
    print("----------------------------------------------------------")


def main():
    """Main function that runs the game."""
    # Score tracking variables
    player_score = 0
    computer_score = 0
    draws = 0
    round_number = 1

    valid_choices = ["rock", "paper", "scissors"]

    # Show welcome message and ask for game mode
    display_welcome()
    mode = select_game_mode()

    if mode == "1":
        print("\n--- Starting Mode: First to 3 Wins ---")
    elif mode == "2":
        print("\n--- Starting Mode: 5-Round Match ---")
    else:
        print("\n--- Starting Mode: Free Play ---")

    # Main game loop
    while True:
        print(f"\n--- Round {round_number} ---")
        player_choice = input(
            "Enter your move (rock/r, paper/p, scissors/s, or quit/q): "
        )

        # Clean up input: remove extra spaces and convert to lowercase
        player_choice = player_choice.strip().lower()

        # Check if the player wants to quit early
        if player_choice == "quit" or player_choice == "q":
            print("\nYou chose to quit the game.")
            break

        # Convert single-letter shortcuts ('r', 'p', 's') to full words
        if player_choice == "r":
            player_choice = "rock"
        elif player_choice == "p":
            player_choice = "paper"
        elif player_choice == "s":
            player_choice = "scissors"

        # Validate the player's input
        if player_choice not in valid_choices:
            print(
                "Invalid move! Please enter 'rock' (r), 'paper' (p), 'scissors' (s), or 'quit' (q)."
            )
            continue

        # Get the computer's move
        computer_choice = get_computer_choice()

        # Display both choices
        print(f"\nPlayer chose   : {player_choice.capitalize()}")
        print(f"Computer chose : {computer_choice.capitalize()}")

        # Determine the winner of the round
        result = decide_winner(player_choice, computer_choice)

        # Announce the round result and update scores
        if result == "draw":
            print("Round Result   : It's a Draw!")
            draws = draws + 1
        elif result == "player":
            print("Round Result   : You win this round!")
            player_score = player_score + 1
        else:
            print("Round Result   : Computer wins this round!")
            computer_score = computer_score + 1

        # Show updated scoreboard
        display_scoreboard(player_score, computer_score, draws)

        # Check if the match is over based on the selected game mode
        if mode == "1" and (player_score == 3 or computer_score == 3):
            print("\nMatch finished! Someone reached 3 wins.")
            break
        elif mode == "2" and round_number == 5:
            print("\nMatch finished! All 5 rounds completed.")
            break

        # Move to the next round
        round_number = round_number + 1

    # Display final results at the end of the game
    print("\n==========================================================")
    print("                      FINAL RESULTS")
    print("==========================================================")
    print(f"   Player Score   : {player_score}")
    print(f"   Computer Score : {computer_score}")
    print(f"   Total Draws    : {draws}")
    print("----------------------------------------------------------")

    if player_score > computer_score:
        print("   WINNER: Congratulations! You won the match!")
    elif computer_score > player_score:
        print("   WINNER: Computer won the match! Better luck next time.")
    else:
        print("   RESULT: The match ended in a tie!")

    print("   Thanks for playing!")
    print("==========================================================")


# Start the program
if __name__ == "__main__":
    main()
