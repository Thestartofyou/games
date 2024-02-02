import random

def non_cooperative_game(player1_action, player2_action):
    # Payoffs for the non-cooperative game
    if player1_action == 'High' and player2_action == 'High':
        return (3, 3)   # Both players choose High - mutual benefit
    elif player1_action == 'High' and player2_action == 'Low':
        return (0, 5)   # Player 1 chooses High, Player 2 chooses Low - Player 1 receives lower payoff
    elif player1_action == 'Low' and player2_action == 'High':
        return (5, 0)   # Player 1 chooses Low, Player 2 chooses High - Player 2 receives lower payoff
    elif player1_action == 'Low' and player2_action == 'Low':
        return (1, 1)   # Both players choose Low - mutual benefit, but less than mutual High

def play_game():
    # Players' strategies
    strategies = ['High', 'Low']

    # Randomly choose strategies for both players
    player1_strategy = random.choice(strategies)
    player2_strategy = random.choice(strategies)

    # Get payoffs based on the chosen strategies
    payoffs = non_cooperative_game(player1_strategy, player2_strategy)

    # Display the results
    print(f"Player 1 chose: {player1_strategy}")
    print(f"Player 2 chose: {player2_strategy}")
    print(f"Payoffs: Player 1 gets {payoffs[0]}, Player 2 gets {payoffs[1]}")

    return payoffs

if __name__ == "__main__":
    play_game()
