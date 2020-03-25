# game.py

import random
from typing import List, Tuple, Sequence, TypeVar

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
Card = Tuple[str, str]
Deck = List[Card]
Choosable = TypeVar("Choosable", str, Card)


def create_deck(shuffle: bool = False) -> List[Card]:
    """Create a new deck of 52 cards."""
    # This line is equivalent to the commented out code below.
    deck = [(s, r) for r in RANKS for s in SUITS]
#   deck = []
#   for r in RANKS:
#       for s in SUITS:
#           deck.append((s, r))
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: List[Card]) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the deck into 4 hands of 13 cards each. The return statement
    returns a tuple of 4 lists of tuples representing each of the 4 players
    hands."""
    return deck[0:28:4], deck[1:28:4], deck[2:28:4], deck[3:28:4]


def choose(items: Sequence[Choosable]) -> Choosable:
    """This method chooses a random item from what may be a list of strings
    for a list of tuples."""
    return random.choice(items)


def player_order(names, start=None):
    """Generates a new list comprised by concatenating slices of the names
    list where first part starts at the selected name index and going to the
    end of the list. The second part starts at the beginning of the list and
    goes to selected name index."""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    print(names[start_idx:])
    print(names[:start_idx])
    return names[start_idx:] + names[:start_idx]


def play() -> None:
    """This is the main function which plays the 4 player card game."""
    my_deck = create_deck(True)
    names = "Terry Hannah Nathan Rebekah".split()
    # This line creates a dictionary with each players name as keys and a
    # list of tuples representing that player's hand.
    hands = {n: h for n, h in zip(names, deal_hands(my_deck))}

    for name, cards in hands.items():
        card_str = " ".join(f"{s}{r}" for s, r in cards)
        print(f"{name}: {card_str}")

    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty.
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
#           print(f"{name}: {card[0] + card[1]}  ", end="")
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()
#   print_deck_hands(my_deck)


def print_deck_hands(deck: Deck) -> None:
    print(deck[0::4])
    print(deck[1::4])
    print(deck[2::4])
    print(deck[3::4])


if __name__ == "__main__":
    play()
