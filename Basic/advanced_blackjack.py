import random

# Define card values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class
class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def reshuffle(self):
        self.__init__()

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ', '.join(str(card) for card in self.cards) + f" (Value: {self.value})"

# Chips Class
class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Game Class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_chips = Chips()

    def take_bet(self):
        while True:
            try:
                bet = int(input(f"You have ${self.player_chips.total}. Enter your bet: "))
                if bet > self.player_chips.total:
                    print("Insufficient chips!")
                else:
                    self.player_chips.bet = bet
                    break
            except ValueError:
                print("Enter a valid number!")

    def hit(self, hand):
        hand.add_card(self.deck.deal_one())

    def player_turn(self, hand):
        while True:
            choice = input("Do you want to Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                self.hit(hand)
                print("Player's Hand:", hand)
                if hand.value > 21:
                    return False
            elif choice == 's':
                return True

    def dealer_turn(self, hand):
        while hand.value < 17:
            self.hit(hand)
        print("Dealer's Hand:", hand)
        return hand.value <= 21

    def compare_hands(self, player_hand, dealer_hand):
        if player_hand.value > 21:
            print("Player busts!")
            self.player_chips.lose_bet()
        elif dealer_hand.value > 21 or player_hand.value > dealer_hand.value:
            print("Player wins!")
            self.player_chips.win_bet()
        elif player_hand.value < dealer_hand.value:
            print("Dealer wins!")
            self.player_chips.lose_bet()
        else:
            print("Push - it's a tie!")

    def play_round(self):
        if len(self.deck.all_cards) < 10:
            print("Reshuffling the deck...")
            self.deck.reshuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(self.deck.deal_one())
        player_hand.add_card(self.deck.deal_one())
        dealer_hand.add_card(self.deck.deal_one())
        dealer_hand.add_card(self.deck.deal_one())

        print("\nDealer shows:", dealer_hand.cards[0])
        print("Player's Hand:", player_hand)

        self.take_bet()
        if self.player_turn(player_hand):
            print("\nDealer's Turn:")
            if not self.dealer_turn(dealer_hand):
                print("Dealer busts!")
                self.player_chips.win_bet()
            else:
                self.compare_hands(player_hand, dealer_hand)
        else:
            print("Player busts!")
            self.player_chips.lose_bet()

        print(f"\nChips left: ${self.player_chips.total}")

    def start_game(self):
        print("Welcome to Advanced Blackjack!\n")
        while self.player_chips.total > 0:
            self.play_round()
            cont = input("\nDo you want to play another round? (y/n): ").lower()
            if cont != 'y':
                break
        print("\nThanks for playing! Your final chip count:", self.player_chips.total)


# Run the game
if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()
