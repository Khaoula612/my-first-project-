secret_number = 4
guess=int(input("guess the number: "))
if guess < secret_number:
  print("the number is greater than your guess")
elif guess > secret_number:
  print("the number is smaller than your guess")
else: 
  print("congratulations!you guessed it right")
  
