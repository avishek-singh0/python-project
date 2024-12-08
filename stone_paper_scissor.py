import random



optins =  ['stone','paper','scissor']
user_win = 0
computer_win=0
while True:
    user_input = input('Select From Stone/Paper/Scissor or quit type q :').lower()
    if user_input == 'q':
      break  
    if user_input not in optins:
       continue
    random_number = random.randint(0,2)
    computer_picked = optins[random_number]
    print("Computer Picked" , computer_picked)

    if user_input == 'stone' and  computer_picked == 'scissor':
        
        print("You won")
        user_win +=1
    elif user_input == 'paper' and  computer_picked == 'stone':
        
        print("You won")
        user_win +=1
    elif user_input == 'scissor' and  computer_picked == 'paper':
        
        print("You won")
        user_win +=1 
    elif user_input == computer_picked:
        print("It's a tie!")  
          
    else:
         print('you lost')
         computer_win += 1
      
print("You won by", user_win)
print("computer win by" , computer_win)
print("Goodby")