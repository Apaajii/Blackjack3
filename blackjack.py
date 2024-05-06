import random


# Funktion för att skapa en kortlek
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


# Funktion för att räkna ut totalvärdet av min hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(rank)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


# Funktion för att visa handen
def display_hand(hand, player):
    print(f"{player}'s Hand:")
    for card in hand:
        print(card[0])


# Spellogik för Blackjack
def play_blackjack():
    while true:
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]


         # Visa spelarens första kort och alla dealerens kort
        print("Dealern hand:")
        print(dealer_hand[0][0])
        print("Din hand:")
        for card in player_hand:
            print(card[0])
            
            # Spelaren hit eller stand
            while calculate_hand_value(player_hand) < 21:
                action = input ("Do you want to hit or stand? h/s: "). lower()
                if action == 'h':
                    player_hand.append(deck.pop())
                    print("Din hand:")
                    for card in player_hand:
                        print(card[0])
                elif action == 's':
                    break
                else:
                    print("Invalid input! Var snäll och välj 'h' för hit eller 's' för stand.", 
                    " to stand.")


               #Dealer Bust
                if calculate_hand_value(player_hand) > 21:
                   print ("Bust! Du förlorade.")
                else:
                        
                        #Dealer hit
                        while calculate_hand_value(dealer_hand) < 17:
                               dealer_hand.append(deck.pop())
                        print ("Dealer's Hand:")   
                        for card in dealer_hand:
                            print (card[0])

                            #Resultat
                            player_score = calculate_hand_value(player_hand)
                            dealer_score = calculate_hand_value(dealer_hand)
                            if player_score > dealer_score or dealer_score  > 21:
                                print ("Du vann!")
                            elif player_score < dealer_score:
                                print ("Dealern vinner!")
                            else:
                                print ("Det blev lika!")   
  
                       


                        
# Starta spelet
play_blackjack()











