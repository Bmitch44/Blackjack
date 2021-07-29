import random

start = input("Do you want to play 21? ").lower()

if start == "yes":
    deck = []
    player_hand = []
    player_score = 0
    player_chips = 500
    dealer_hand = []
    dealer_score = 0

    while True:
        start_game = input("\nType s to start or q to quit: ").lower()
        if start_game == "s":
            # creates deck
            for s in range(4):
                for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]:
                    deck.append(v)

            # shuffles deck
            random.shuffle(deck)

            print(f"\nYou now have a balance of: {player_chips} chips\n")
            while True:
                try:
                    bet = float(input("How much do you want to bet? "))
                    break
                except ValueError:
                    print("Please type a number")
            player_chips -= bet
            print(f"\nNew balance: {player_chips}")

            # deals first two player and dealer cards
            for i in range(0, 2):
                player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

            print(f"\nYour cards: {player_hand}")
            print(f"dealer cards: {dealer_hand} and X")
            dealer_hand.append(deck.pop())

            # gets player and dealer scores
            player_score += sum(player_hand)
            dealer_score += sum(dealer_hand)

            if 1 in player_hand or dealer_hand:
                if player_score <= 11:
                    player_score += 10
                elif dealer_score <= 11:
                    dealer_score += 10

            # if player gets blackjack on first 2 cards
            if player_score == 21 and dealer_score != 21:
                print("Blackjack! You win")
                player_chips += bet * 2.5
                print(f"New Balance: {player_chips}")
            else:
                print(f"\nYour score: {player_score}\n")
                break
        else:
            print("Have a nice day!")
            quit()

    # deals to the player every time they type "hit", then deals to dealer and evaluates
    while True:
        prompt = input("Hit or Stay ").lower()
        if prompt == "hit":
            player_hand.append(deck.pop())
            player_score += player_hand[-1]
            print(f"\nYour cards: {player_hand}")
            print(f"Your score: {player_score}\n")

            if player_score == 21:
                while dealer_score < 17:
                    dealer_hand.append(deck.pop())
                    dealer_score += dealer_hand[-1]
                else:
                    if player_score > dealer_score and dealer_score < 21:
                        print(f"\nBlackjack! You win with {player_score}")
                        player_chips += bet * 2
                        print(f"New Balance: {player_chips}")
                    else:
                        print("Tie!")
                        player_chips += bet
            elif player_score > 21:
                print("Bust, dealer wins")
                break

        else:
            print(f"\nYou finished with {player_score}")
            while dealer_score < 17:
                dealer_hand.append(deck.pop())
                dealer_score += dealer_hand[-1]
            else:
                if player_score > dealer_score:
                    print("\nYou win!")
                    player_chips += bet * 2
                    print(f"New Balance: {player_chips}")
                    break
                elif dealer_score > 21:
                    print("You win, dealer busted")
                    player_score += bet * 2
                    print(f"New Balance: {player_chips}")
                    break
                elif player_score < dealer_score:
                    print(f"\nDealer wins, with a score of {dealer_score}")
                    break
                else:
                    print("\nTie")
                    break
else:
    print("Have a nice day!")
    quit()