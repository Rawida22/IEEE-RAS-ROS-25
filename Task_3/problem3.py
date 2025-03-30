import random
 
low =1 
High = 100
guesses =0 
random_num = random.randint(low,High)
while True:
 guess= int(input("Enter number between {low} - {High}: "))
 guesses = guesses +1
 if guess < random_num:
   print(f"{guess} is too low!")
 elif guess > random_num:
   print(f"{guess} is too High!")
 else:
   print(f"{guess} is correct!")       
   break
print(f"this round took you {guesses} guesses") 