import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return "{}".format(self.rank) + " of " + "{}".format(self.suit)


class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))
	def __str__(self):
		deck_comp = ""
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return "The deck has" + deck_comp
	def shuffle(self):
		random.shuffle(self.deck)
	def deal(self):
		single_card = self.deck.pop(0)
		return single_card
	def checkDeck(self):
		print(self.deck)


class Hand:
	def __init__(self):
		self.card = []
		self.value = 0
		self.aces = 0
	def add_card(self, single_card):
		self.card.append(single_card)
		return self.card
	def adjust_for_ace(self):
		pass


class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0
	def win_bet(self):
		pass
	def lose_bet(self):
		pass

test_deck = Deck()
my_hand = Hand()
dealer_hand = Hand()
my_chips = Chips()

def startGame():
	test_deck.shuffle()
	my_chips.bet = bet()
	print("The user has bet $" + str(my_chips.bet) + ". The dealer deals two cards to each player\n")
	my_hand.add_card(test_deck.deal())
	dealer_hand.add_card(test_deck.deal())
	my_hand.add_card(test_deck.deal())
	dealer_hand.add_card(test_deck.deal())

def calculateHands():
	resetValues()
	print("\nYour cards are: ")
	for card in range(len(my_hand.card)):
		print(my_hand.card[card])
	for card in my_hand.card:
		my_hand.value += values[card.rank]

	#Comment out unless to debug
	print(my_hand.value)

	print("\nThe dealer's is showing: ")
	print(dealer_hand.card[0])	
	for card in dealer_hand.card:
		dealer_hand.value += values[card.rank]

	#Comment out unless to debug
	print(dealer_hand.value)

def resetValues():
	my_hand.value = 0
	dealer_hand.value = 0

def resetHands():
	my_hand.card = []
	dealer_hand.card = []

def deductLosses():
	my_chips.total -= my_chips.bet

def addWinnings():
	my_chips.total += my_chips.bet

def bet():
	print("You have $" + str(my_chips.total) + ".")
	user_bet = input("How much would you like to wager? ")
	return int(user_bet)

def hitOrStay():
	user_choice = input("\nWould you like to hit or stay? ")
	if user_choice == "hit":
		my_hand.add_card(test_deck.deal())
		calculateHands()
		checkBust()
	if user_choice == "stay":
		dealerTurn()
		determineWinner()
		
def dealerTurn():
	calculateHands()
	while dealer_hand.value < 17:
		print("\nDealer hits\n")
		dealer_hand.add_card(test_deck.deal())
		calculateHands()
	if dealer_hand.value > 21:
		showHands()
		print("\nDealer busts! You win!")
		addWinnings()
		print("Your bank has $" + str(my_chips.total) + ".")
		playAgain()
	else:
		print("\nDealer stays.\n")
		showHands()

def playAgain():
	answer = input("Would you like to play again? ")
	if answer == "yes":
		resetValues()
		resetHands()
		playBlackjack()
	elif answer == "no":
		print("Thanks for playing!")

def checkBust():
	if my_hand.value > 21:
		print("BUST!")
		deductLosses()
		print("Your bank has $" + str(my_chips.total) + ".")
		playAgain()
	else:
		hitOrStay()


def determineWinner():
	if dealer_hand.value <= 21:
		if my_hand.value > dealer_hand.value:
			addWinnings()
			print("\nYou win! Your bank has $" + str(my_chips.total) + ".")
			playAgain()
		else:
			deductLosses()
			print("\nDealer wins. Better luck next time.\n")
			print("Your bank has $" + str(my_chips.total) + ".")
			playAgain()

def showHands():
	resetValues()
	print("Your cards are: ")
	for card in range(len(my_hand.card)):
		print(my_hand.card[card])
	print("\n")
	for card in my_hand.card:
		my_hand.value += values[card.rank]

	print("The dealer's cards are: ")
	for card in range(len(dealer_hand.card)):
		print(dealer_hand.card[card])
	for card in dealer_hand.card:
		dealer_hand.value += values[card.rank]

def playBlackjack():
	startGame()
	calculateHands()
	checkBust()

playBlackjack()