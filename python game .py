import random
def game():
    import pyttsx3
    h=pyttsx3.init()
    score=random.randint(0,100)
    print("your score is:",score)
    with open("hscore.txt","r") as f:
        high=f.read()
    if(high!=""):
        high=int(high)
    else:
       high=0
    if(score>high):
       print("new high score is:",score)
       print("congratulation! you have beaten the high score")
       h.say("congratulation! ")
    else:
         print("your high score is:",high)
         print("better luck next time")
         h.say("better luck next time")
    h.runAndWait()
    with open("hscore.txt","w") as f:
        f.write(str(max(score,high)))
game()             
              