import random

print('Rock, Paper, Scissors --Shoot!!')
trials=input('How many times do you wish to compete? ')

matches=0
while matches <int(trials):
    
    player_choice = input('Choose your weapon [R]ock], [P]aper, or [S]cissors: ')
    print(f'You chose: {player_choice} ')


    choices=['R','P','S']
    opponent_choice = random.choice(choices)
    print(f'I chose {opponent_choice}')


    if opponent_choice == str.upper(player_choice):
        print ("Tie! ")
        matches+=1
    
    elif opponent_choice == 'R' and player_choice.upper() == 'S':      
        print ("Scissors beats rock, I win! ")
        matches+=1
    
    elif opponent_choice == 'S' and player_choice.upper() == 'P':      
        print ("Scissors beats paper! I win! ")
        matches+=1
    
    elif opponent_choice == 'P' and player_choice.upper() == 'R':      
        print ("Paper beat rock, I win! ")
        matches+=1

    
