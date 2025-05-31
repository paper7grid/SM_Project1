print("Hello Welcome to my World Quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
answer = input("What is the capital of India? ").lower()
if answer == "delhi":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Delhi")
answer == input("What is the capital of USA? ").lower()
if answer == "washington d.c.":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Washington D.C.")
answer = input("What is the capital of Japan? ").lower()
if answer == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Tokyo")
answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Paris")
print("You have completed the quiz! Thank you for playing :)")
print("I hope you enjoyed it!")
print("You got", score, "out of 4 questions correct.")
print("Your score is", (score / 4) * 100, "%")