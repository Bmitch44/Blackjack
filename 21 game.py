import random

start = input("Do you want to play 21 (y/n)? ").lower()

if start[0] == "y":
    player_chips = 500

    while True:
        start_game = input("\nType s to start, c to cash out, or q to quit: ").lower()
        if start_game == "s":
            deck = []
            dealer_hand = []
            dealer_score = 0
            player_hand = []
            player_score = 0
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
                    if bet <= player_chips:
                        player_chips -= bet
                        break
                    else:
                        print("Bet must be less than your balance")
                except ValueError:
                    print("Please type a number")
                # checks if you have enough chips to fulfill the bet

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

            # checks for a 1 which can also have a value of 11
            if 1 in player_hand:
                if player_score <= 11:
                    player_score += 10
            elif 1 in dealer_hand:
                if dealer_score <= 11:
                    dealer_score += 10

            # if player gets blackjack on first 2 cards
            if player_score == 21 and dealer_score != 21:
                print("\nBlackjack! You win")
                player_chips += bet * 2.5
                print(f"\nYou won {bet * 2.5} chips")
                print(f"New Balance: {player_chips}")
            else:
                print(f"\nYour score: {player_score}\n")

                # deals to the player every time they type "hit", then deals to dealer and evaluates
                while True:
                    prompt = input("Hit or Stay ").lower()
                    if prompt[0] == "h":
                        player_hand.append(deck.pop())
                        player_score += player_hand[-1]
                        print(f"\nYour cards: {player_hand}")
                        print(f"Your score: {player_score}\n")

                        # checks for blackjack
                        if player_score == 21:
                            while dealer_score < 17:
                                dealer_hand.append(deck.pop())
                                dealer_score += dealer_hand[-1]
                            else:
                                if player_score > dealer_score and dealer_score < 21:
                                    print(f"\nBlackjack! You win with {player_score}")
                                    player_chips += bet * 2
                                    print(f"\nYou won {bet * 2} chips")
                                    print(f"New Balance: {player_chips}\n")
                                    break
                                else:
                                    print("Tie!")
                                    player_chips += bet
                                    print(f"\nYou won {bet} chips")
                                    print(f"New Balance: {player_chips}\n")
                                    break
                        elif player_score > 21:
                            print("Bust, dealer wins")
                            break

                    # evaluates scores and determines winner
                    else:
                        print(f"\nYou finished with {player_score}")
                        while dealer_score < 17:
                            dealer_hand.append(deck.pop())
                            dealer_score += dealer_hand[-1]

                        else:
                            print(f"Dealer finished with {dealer_score}\n")
                            if player_score > dealer_score:
                                print("You win!")
                                player_chips += bet * 2
                                print(f"\nYou won {bet * 2} chips")
                                print(f"New Balance: {player_chips}")
                                break
                            elif dealer_score > 21:
                                print("You win, dealer busted")
                                player_chips += bet * 2
                                print(f"\nYou won {bet * 2} chips")
                                print(f"New Balance: {player_chips}")
                                break
                            elif player_score < dealer_score:
                                print(f"Dealer wins, with a score of {dealer_score}")
                                break
                            elif player_score > 21:
                                print("Bust, dealer wins")
                            else:
                                print("Tie")
                                print(f"You won {bet} chips")
                                break
        elif start_game == "c":
            print(f"\nCongrats! you won {player_chips} chips!")
            quit()
        elif start_game == "q":
            print("Have a nice day!")
            quit()
        else:
            print("Please type s, q, or c")
else:
    print("Have a nice day!")
    quit()
