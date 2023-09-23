from higher_lower_data import data
from higher_lower_data import logo
from higher_lower_data import vs
from random import randint
import os

random_choice_1=randint(0,len(data)-1)
random_choice_2=randint(0,len(data)-1)

if random_choice_1==random_choice_2:
    random_choice_2=randint(0,len(data)-1)
os.system('cls')
print(logo)
game_end=False
score=0

while not game_end:
    random_choice_2=randint(0,len(data)-1)
    print("Compare : ",end=" ")
    
    print(f"{data[random_choice_1]['name']} a {data[random_choice_1]['description']} from {data[random_choice_1]['country']}")
    
    print(vs)

    print(f"{data[random_choice_2]['name']} a {data[random_choice_2]['description']} from {data[random_choice_2]['country']}")

    guess = int(input("Press '1' for first choice and '2' for second : "))
    answer=0
    
    if data[random_choice_1]['follower_count']>data[random_choice_2]['follower_count']:
        answer=1
    else:
        answer=2

    if(guess == answer):
        print("You're Correct")
        game_end=False
        score+=1
        if(guess==2):
            random_choice_1=random_choice_2
        os.system('cls')
    
    else:
        game_end=True

print("Game end")
print(f"Your score is : {score}")

