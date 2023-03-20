from random import randint

print("Rock Paper Scissors Game")

random_num = randint(0, 3)

if random_num == 0:
    Bot = "rock"
elif random_num == 1:
    Bot = "paper"
else:
    Bot = "scissors"
player = input("player : ").lower()

if player == Bot:
    print("Bot: ",Bot)
    print("Tie")
    
elif player == "rock":
    if Bot == "paper":
        print("Bot: ",Bot)
        print("You Lose")
    else:
        print("You Win")
elif player == "scissor":
    if Bot == "rock":
        print("Bot: ",Bot)
        print("You Lose")
    else:
        print("You Win")
elif player == "paper":
    if Bot == "scissors":
        print("Bot: ",Bot)
        print("You win")
    else:
        print("Bot: ",Bot)
        print("You Lose")
else:
    print("you move is not valid")