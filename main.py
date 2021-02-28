cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from replit import clear
from art import logo

def end_game():
  print(f"Your final hand is {player_hand}, the final score is {score_player}.")
  print(f"Computer's final hand is {computer_hand}, the final score is {score_computer}.")

def show_hand():
  print(f"Your card is {player_hand}, current score is {score_player}")
  print(f"Computer's first card is {com_first_hand}")

def draw_card():
  card = random.choice(cards)
  return card

def if_ace(hand):
  index = hand.index(11)
  hand[index] = 1
  return hand

def win_lose(score_player, score_computer):
  if score_player > 21:
    end_game()
    print("You were busted. You lose.")
  elif score_computer > 21:
    end_game()
    print("The computer was busted. You win.")
  elif score_player > score_computer:
    end_game()
    print("You win.")
  elif score_player < score_computer:
    end_game()
    print("You lose")
  elif score_player == score_computer:
    end_game()
    print("Draw")

while input("Do you want to play blackjack? Type 'y' or 'n' : ") == "y":
  clear()
  print(logo)
    
  player_hand = []
  computer_hand = []

  for i in range(2):
    player_hand.append(draw_card())
    computer_hand.append(draw_card())
    score_player = sum(player_hand)
    score_computer = sum(computer_hand)

  com_first_hand = computer_hand[0]

  if score_player == 21:
    end_game()
    print("You win! You got a Blackjack!")
  elif score_computer == 21:
    end_game()
    print("You lose! Computer got a Blackjack!")
  else:
    show_hand()
    pass_game = False

    while score_player <= 21 and pass_game == False:
      draw = input("Type 'y' if you want to draw, type 'n' to pass: ")
      if draw == 'y':
        player_hand.append(draw_card())
        score_player = sum(player_hand)
        show_hand()
      elif draw == 'n':
        pass_game = True
      else:
        print("Please type valid choice. 'y' or 'n'")
    
    if score_player > 21 and 11 in player_hand:
      if_ace(player_hand)
      score_player = sum(player_hand)
    
    while score_computer <= 16:
      computer_hand.append(draw_card())
      score_computer = sum(computer_hand)
    
    if score_computer > 21 and 11 in computer_hand:
      if_ace(computer_hand)
      score_computer = sum(computer_hand)

    win_lose(score_player,score_computer)




    
