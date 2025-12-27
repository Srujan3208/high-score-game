import random
import pyttsx3
import os

def game():
    engine = pyttsx3.init()
    score = random.randint(0, 100)
    print("Your score is:", score)

    if os.path.exists("hscore.txt"):
        with open("hscore.txt", "r") as f:
            high = f.read()
            high = int(high) if high else 0
    else:
        high = 0

    if score > high:
        print("New high score is:", score)
        print("Congratulations! You have beaten the high score 🎉")
        engine.say("Congratulations! You have beaten the high score")
        high = score
    else:
        print("Your high score is:", high)
        print("Better luck next time")
        engine.say("Better luck next time")

    engine.runAndWait()

    with open("hscore.txt", "w") as f:
        f.write(str(high))

game()
