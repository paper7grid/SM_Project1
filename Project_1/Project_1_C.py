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
answer == input("What is the capital of China? ").lower()
if answer == "Hong Kong":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Hong Kong")
answer = input("What is the capital of Russia? ").lower()
if answer == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Moscow")
answer = input("What is the capital of Australia? ").lower()
if answer == "canberra":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Canberra")
answer = input("What is the capital of Canada? ").lower()
if answer == "ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Ottawa")
print("You have completed the quiz! Thank you for playing :)")
print("I hope you enjoyed it!")
print("You got", score, "out of 8 questions correct.")
print("Your score is", (score / 8) * 100, "%")