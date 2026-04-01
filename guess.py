import random

def guess(x):
  num = random.randint(1,x)
  guess = 0
  while guess != num:
    guess = int(input("enter your guess : "))
    if guess < num:
      print("tooo low")
    elif guess > num:
      print("too high")

  print(f"you guessed the correct number {num}")

guess(100)
