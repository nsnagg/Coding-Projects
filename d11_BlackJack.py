import random


def deal_card():
    cards: int = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    # print(selected_card)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif p_score == 0:
        return "Win with a Blackjack"
    elif p_score > 21:
        return "You went over. You lose 😒"
    elif c_score > 21:
        return "Opponent went over. You win 😊"
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose 😒"


def play_game():
    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1
    is_game_over = False

    # Deal initial 2 cards
    for _ in range(2):
        new_card = deal_card()
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to hold: ")
            print("\n" * 2)
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n")
    print(f"Your score: {player_score} your cards: {player_cards}")
    print(f"Computer score: {computer_score} computer cards: {computer_cards}")

    print(compare(player_score, computer_score))


while input("Do you want to play a game of Black Jack? 'y' for yes 'n' for no: ") == "y":
    print("\n" * 20)
    play_game()

