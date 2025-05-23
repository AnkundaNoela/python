'''count = 1
while count <= 5:
    print(count)
    count +=1 '''
    
count = 1
while count <= 5:
    if count ==4:
        break
    print(count)
    count +=1   
    
    #skip 3
    i=0
    while i<5:
        i +=1
        if i==3:
            continue
        print(i) 
    
    
   # generate a random no between 1 and 10 ask the user to guess until they are right
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Loop until the user guesses correctly
while True:
    guess = input("Guess a number between 1 and 10: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess == secret_number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print("Wrong guess. Try again.")
