
import random

print("""
Welcome to the Coin Guessing Game!
Chooce a method to toss the coin:
1-Using random.random()
2-Using random.randint()""")

choice=int(input('Entre your choice (1 or 2):'))
guess=input('Entre your Guess (Heads or Tails)').lower()

random_1=random.random()
ran=random_1>=0.5


random_2=random.randint(0,1)

if choice==2:
    if random_2==0:
        computer="Heads"
    else:
        computer="Tails"

elif choice==1:
    if ran:
        computer="Heads"
    else:
        computer="Tails"
else:
    print("Invalid choice please enter 1 or 2")

if guess==computer.lower():
    print("Congatulations!You win")
else:
    print('Sorry you lost')
    print(f'The computer {computer}')

    

