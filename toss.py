import random

coin=["Heads","Tails"]
toss=random.choice(coin)
selection=input("heads or Tails: ")

if selection==toss:
    print("You Win! The coin landed on ",toss)
else:
    print("You Lose! The coin landed on ",toss)
