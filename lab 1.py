from random import shuffle

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


def create_deck():
    """Return a list of 52 unique cards

    Each list item should be a dictionary of the form:

    {
        rank: "2",
        suit: "Hearts",
    }
    """
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append({'rank': rank, 
                         'suit': suit})
    return deck



assert len(create_deck()) == 52
assert create_deck()[0]["rank"] in ranks
assert create_deck()[13]["suit"] in suits
assert len(set(map(str, create_deck()))) == 52
assert create_deck() is not create_deck()


def deal(deck):
    """Return a tuple containing a list of cards for each player

    Cards are given to players one at a time from the front of the list

    For example, assuming `deck` is a list of 6 cards, the function should
    return a tuple contain two lists of three cards each. The cards in each
    list should be "drawn" in order from the front of the `deck`.
    """
    player1 = []
    player2 = []

    for i, card in enumerate(deck):
        if i % 2 == 0:
            player1.append(card)
        else:
            player2.append(card)
    
    return player1, player2






assert deal([2, 3]) == ([2], [3])
assert deal([2, 3, 4, 5]) == ([2, 4], [3, 5])
assert len(deal(create_deck())[0]) == 26
assert len(deal(create_deck())[1]) == 26


def battle(player_card, opponent_card):
    """
    Return result of a battle between two cards

    If the `player_card` rank is higher, return "win"
    If the `player_card` rank is lower, return "loss"
    If the `player_card` rank is equal, return "tie"
    """
    rank_values = {rank: i for i, rank in enumerate(ranks)}
    if rank_values[player_card['rank']] > rank_values[opponent_card['rank']]:
        return('win')
    elif rank_values[player_card['rank']] < rank_values[opponent_card['rank']]:
        return('loss')
    else:
        return('tie')

assert battle({"rank": "Queen"}, {"rank": "Queen"}) == "tie"
assert battle({"rank": "King"}, {"rank": "Queen"}) == "win"
assert battle({"rank": "Jack"}, {"rank": "Queen"}) == "loss"
assert battle({"rank": "Ace"}, {"rank": "Queen"}) == "win"
assert battle({"rank": "3"}, {"rank": "2"}) == "win"

# Complete the program so that it will simulate a game of our version of War between two players
def play_game():
    deck = create_deck()
    shuffle(deck)


    player1_hand , player2_hand = deal(deck)

    player1_wins = 0
    player2_wins = 0
    ties = 0

    for player1_card, player2_card in zip(player1_hand, player2_hand):
        print(f"Player 1 draws {player1_card['rank']} of {player1_card['suit']}")
        print(f"Player 2 draws {player2_card['rank']} of {player2_card['suit']}")
        result = battle(player1_card, player2_card)

        if result =='win':
            print('Player 1 wins!')
            player1_wins +=1
        elif result == 'loss':
            print('Player 2 wins!')
            player2_wins += 1
        else:
            print('Its a tie!')
            ties += 1
        print()

    print('Game summary')
    print(f'Player 1 won {player1_wins} times. Player 1 lost {player2_wins} times. Tied {ties} times.')
    print(f'Player 2 won {player2_wins} times. Player 2 lost {player1_wins} times. Tied {ties} times.')
play_game()
# See readme.md for more details