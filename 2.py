# Number Guessing Game
import random 
top_of_range = input('Type a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number greater than zero next time.')
        quit()
else:
    print('Type a number next time.')
    quit()
random_number = random.randint(0, top_of_range)
print(random_number)
guesses = 0

while True:
    guesses += 1 
    user_guess = input('Type a number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Type a number next time.')
        continue
    print("after continue")

    if user_guess == random_number :
        print('You got it!')
        break
    elif user_guess > random_number :
        print('You are above the number!')
    else: 
        print('You are below the number!')

print("You got it in", guesses ,"guesses" )