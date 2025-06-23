import random

money = 100
symbols = "🍒", "💎", "💀"
def slots():
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)
    slots = (f"{slot1} {slot2} {slot3}")
    print(slots)
    return slot1, slot2, slot3
while True:
    play = input("Do you want to play a slot machine? Y/N ")
    if play == "n":
        print("Ok, bye.")
        playing = False
        break
    elif play != "n" and play != "y":
        print("You have to type 'Y' or 'N'!")
        continue
    elif play == "y":
        playing = True
        break
while playing == True:
    print(f"Your wallet: {money}$")

    while True:
        try:
            bet = int(input("Enter the amount you want to bet: "))
            if bet > money:
                print("You don't have so much money!")
                print(f"Your wallet: {money}")
                continue
            elif bet <= 0:
                    print("You can't bet nothing!")
            elif bet <= money:
                    break
        except ValueError:
                print("You have to type a normal number!")


    money -= bet
    slot1, slot2, slot3 = slots()
    if slot1 == slot2 == slot3:
        bet = bet * 5
        money = bet + money
        print("You got x5 money of your bet")
        print(f"You got {bet}$")
        print(f"Your wallet: {money}$")
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        bet = bet * 2
        money = bet + money
        print("You got x2 money of your bet")
        print(f"You got {bet}$")
        print(f"Your wallet: {money}$")
    else:
        print(f"You lose {bet}$")
        print(f"Your wallet: {money}$")
    if money <= 0:
        print("You're broke! Game over.")
        break
    while True:
        play_again = input("Do you want to play again? Y/N ")
        if play_again == "y":
            break
        elif play_again == "n":
            print("Okay, bye.")
            playing = False
            break
        else:
            print("You have to type 'Y' or 'N'!")
            continue
