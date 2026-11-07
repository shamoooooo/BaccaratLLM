import random
from openai import OpenAI


def bscore():
    banker = random.randint(1,10)
    if banker == 10:
        banker = 0
    return banker

def pscore():
    player = random.randint(1,10)
    if player == 10:
        player = 0
    return player

def result(player,banker):
    if player > banker:
          final = 'P'
    elif banker > player:
         final = 'B'
    else:
         final = 'T'
    return final

client = OpenAI()

prompt = '''Predict the next outcome based on the information in this .txt file. 
GOAL: 
Predict the next outcome in a hand of Bacarrat. Analyze the file and attempt to find patterns if possible. 
The results of the bacarrat simulator are recorded by entering the end result of a round to the .txt supplied
Depending on the result, the information entered to the file will be either P, B, or T.
KEY:
P = Player
B = Banker
T = Tie
EXAMPLE:
If the value of player is higher than banker, then the information entered to the .txt file is P. If the values are equal, then T. If the banker is greater than player, 
then B is entered.
'''

COMMISSION = 0.05
seperator = '-'*20
count = 0

play_question = input('Would you like to play baccarat? ')

if play_question == 'Yes' or play_question == 'yes':
    play = True
else:
    play = False

print(seperator)

with open('Bacarrat_Results.txt','a+') as file:
    

    bankroll = float(input('Enter bankroll: $'))
    
    print(seperator)

    while play and bankroll>0:

        file.seek(0)
        contents = file.read()
        
        bet = float(input('Enter wager: $'))

        print(seperator)

        while bet > bankroll:
            bet = float(input('Bet cannot be more than bankroll. Enter a valid bet: $'))
            print(seperator)

        print('Enter the side you would like to wager')
        side_selection = input('Enter p or P for player and b or B for banker: ')
        side = side_selection[0]
        print(seperator)

        if side == 'b' or side == 'B':
            print('Note that banker wins owe 5 percent commission')
            print(seperator)

        response = client.responses.create(
                model="gpt-5.2",
                input=f"""
                    Here are the contents of my text file:
        
                    {contents}
        
                    Answer this question using the file:
                    {prompt}
                    """
                    )
        
        print('CHATGPT PREDICTED RESULT:')
        print(seperator)
        print(response.output_text)
        
        player = pscore()
        banker = bscore()

        
        count+=1
        
        banker_win = bet - (bet*COMMISSION)
        
        if banker > player:
            if side == 'b' or side == 'B':
                bankroll += bet-(bet*COMMISSION)
                print(f'Banker win.\nCongrats! You won ${banker_win:.2f}. Your bankroll is now ${bankroll:.2f}')
                print(seperator)
            else:
                bankroll -= bet
                print(f'Player win.\n${bet:.2f} is subtracted from your bankroll. ${bankroll:.2f} remains.')
                print(seperator)
        elif player > banker:
            if side == 'b' or side == 'B':
                bankroll -= bet
                print(f'Player win.\n${bet:.2f} is subtracted from your bankroll. ${bankroll:.2f} remains.')
                print(seperator)
            else:
                bankroll+=bet
                print(f'Player win.\nCongrats! You won ${bet:.2f}. Your bankroll is now ${bankroll:.2f}')
                print(seperator)
        else:
            print(f'Tie hand. No change to bankroll.')
            print(seperator)

          
        


        file.write(result(player,banker))
        
        if bankroll <= 0:
                break
        
    
    
        if play_question == 'Yes' or play_question == 'yes':
            play = True
        else:
            play = False
    
    
    
    
    
if count > 1:
        duration = 'hands'
else:
        duration = 'hand'

print(f'Thanks for playing! You lasted {count} {duration}.')

    

    
