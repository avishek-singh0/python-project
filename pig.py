import random

def roll():
      min_number = 1
      max_number = 6
      roll = random.randint(min_number,max_number)

      return roll

while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:             
             break
        else:
             print("Must be betwen 2-4 players")
    else:
         print("Invaild,try again")

max_score  = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

 for  player_idx in range(players):
    print("Player",player_idx+1,'turn has hust started')     

    current_score = 0
    while True:
      should_roll = input("Would You like to roll (y) ")
      if should_roll.lower() != 'y':
           break
      
      value = roll()
      if value == 1:
           print("You should a 1 ! Turn done! ")
           current_score = 0
           break
      else:
           current_score += value
           print('You rolled',value)
      
      print("Your Score is:",current_score)

    player_scores[player_idx] +=current_score
    print("Your total score is:",player_scores[player_idx])

