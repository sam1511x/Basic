# Quiz Game
print("Welcome to the QUIZ")
playing = input("Do you want to play the Quiz? ")
print(playing)
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")
score=0
answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print('Incorrect')

answer = input("What does ROM stands for? ").lower()
if answer == "read only memory":
    print("Correct")
    score += 1
else:
    print('Incorrect')

answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")