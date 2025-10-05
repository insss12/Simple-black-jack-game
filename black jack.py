#simple black jack game
import random

points=0
n = 0

def generate():
    generate_number=random.randint(18, 23)
    return generate_number

def player_option():
    choices=random.randint(1, 7)
    return choices

def take_1(choices):
    return choices

def take_2(choices):
    return choices

def game_start():
    print("pick 1 or 2 cards")
    try:
        pick=int(input())
        if pick == 1:
            choice=player_option()
            result=take_1(choice)
            return result

        elif pick == 2:
            choice=player_option()
            result_1=take_2(choice)
            result_2=take_2(choice)
            total=result_1+result_2
            return total
        else:
            return 0
    except ValueError:
        print("please return a valid number")
        return 0

print("*******************************")
print("welcome to the black jack game")
print("*******************************")
print(f"The dealer's card is hidden. Try to get close to the number as possible")
print("do you want to play ? [yes/no]")
player_choice = input().lower()

while player_choice == "yes" and n < 4:
    if player_choice == "yes":
        round_point=game_start()
        points+=round_point
        n+=1
        print(f"you got {points}")
        print("do you wish to continue [yes/no]")
        player_choice2=input().lower()
        if player_choice2 == "no":
            break

hidden_card=generate()
print(f"The card was.....{hidden_card}")
if points > generate():
    print(f"your number was higher than the hidden card by {points-hidden_card}")
elif points < generate():
    print(f"Your number was lower than the hidden card by {hidden_card-points}")
else:
    print(f"congrat YOU WON")