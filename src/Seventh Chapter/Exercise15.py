# You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe
# / Noughts and Crosses.
# Your friend will write the logic to play one round of the game,
# while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc.
# The two of you negotiate on how the two parts of the program will fit together,
# and you come up with this simple scaffolding (which your friend will improve later) - see below.

# 1) Write the main program which repeatedly calls this function to play the game,
# and after each round it announces the outcome as “I win!”, “You win!”, or “Game drawn!”.
# It then asks the player “Do you want to play again?” and either plays again, or says “Goodbye”, and terminates.

# 2) Keep score of how many wins each player has had, and how many draws there have been.
# After each round of play, also announce the scores.

# 3) Add logic so that the players take turns to play first.

# 4) Compute the percentage of wins for the human, out of all games played. Also announce this at the end of each round.

def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

def play_game():
    wincount_player = 0
    wincount_comp = 0
    drawcount = 0
    player_turn = True
    while True:
        result = play_once(player_turn)
        if result == -1:
            wincount_player += 1
            print("You win!")
        elif result == 0:
            drawcount += 1
            print("Game drawn!")
        else:
            wincount_comp += 1
            print("I win!")
        player_turn = not player_turn
        print(f"Player wins: {wincount_player}, Computer Wins: {wincount_comp}, Draws: {drawcount}")
        print(f"Player wins percentage: {100*(wincount_player/(wincount_player + drawcount + wincount_comp))}%")
        while True:
            response = input("Do you want to play again? Type y or n")
            if response == "n":
                print("Goodbye!")
                return
            if response == "y":
                break


play_game()
