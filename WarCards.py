import random
#Deck of Cards
class Deck:
    # Initializing the deck
    def __init__(self, total_deck = None):
        self.total_deck = total_deck
        self.num = 2
        self.temp_deck = []
        self.houses = ["Hearts", "Diamonds", "Spades", "Clubs"]
        
    # Generating the deck
    def generating_cards(self):
        while self.num < 11:
            for suit in self.houses:
                self.temp_deck.append([self.num, suit])
            self.num += 1

        for suit in self.houses:
            self.temp_deck.append([13, "King", suit])
            self.temp_deck.append([12, "Queen", suit])
            self.temp_deck.append([11, "Jack", suit])
            self.temp_deck.append([14, "Ace", suit])

        for item in self.temp_deck:
            self.total_deck.append(item)

    def shuffle_deck(self):
        random.shuffle(self.total_deck)
        return self.total_deck
    def deal_deck(self):
        return self.total_deck[:26], self.total_deck[26:]

def main():
    current_deck = Deck()
    current_deck.generating_cards()
    current_deck.shuffle_deck()
    print(current_deck.total_deck)
    player1_deck, player2_deck = current_deck.deal_deck()
    print("Player 1's Deck: ", player1_deck)
    print("Player 2's Deck: ", player2_deck)

main()