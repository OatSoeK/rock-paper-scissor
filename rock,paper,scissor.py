import random

def getChoice():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  opitions = ["rock", "paper", "scissors"]
  computer_choice = random.choice(opitions)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


def check_win(player, computer):
  print("You choose " + player + ", computer choose " + computer)
  if player == computer:
    return "this is a tie"
  elif player == "rock":
    if computer == "scissors":
      return "rock can smash scissors, you win"
    else:
      return "paper can cover rock, you lose"
  elif player == "scissors":
    if computer == "paper":
      return "scissors can cut paper, you win"
    else:
      return "rock can smash scissors, you lose"

  elif player == "paper":
    if computer == "rock":
      return "paper can cover rock, you win"
  else:
    return "scissors can cut paper, You lose!"


choices = getChoice()
result = check_win(choices["player"], choices["computer"])
print(result)
