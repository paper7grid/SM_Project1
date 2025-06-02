print("Hello Welcome to my World Quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
print("What is the capital of India? ")
print("a) Mumbai\nb) Delhi\nc) Kolkata\nd) Chennai")
answer = input("Your answer: ").lower()
if answer == "b" or answer == "delhi":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Delhi")
print("What is the capital of USA? ")
print("a) New York\nb) Washington D.C.\nc) Los Angeles\nd) Chicago")
answer = input("Your answer: ").lower()
if answer == "b" or answer == "washington d.c.":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Washington D.C.")
print("What is the capital of Japan? ")
print("a) Tokyo\nb) Osaka\nc) Kyoto\nd) Hiroshima")
answer = input("Your answer: ").lower()
if answer == "a" or answer == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Tokyo")
print("What is the capital of France? ")
print("a) Paris\nb) Lyon\nc) Marseille\nd) Nice")
answer = input("Your answer: ").lower()
if answer == "a" or answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Paris")
print("What is the capital of China? ")
print("a) Shanghai\nb) Hong Kong\nc) Beijing\nd) Shenzhen")
answer = input("Your answer: ").lower()
if answer == "c" or answer == "beijing":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! the correct answer is Hong Kong")
print("What is the capital of Russia? ")
print("a) Moscow\nb) St. Petersburg\nc) Novosibirsk\nd) Yekaterinburg")
answer = input("Your answer: ").lower()
if answer == "a" or answer == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Moscow")
print("What is the capital of Australia? ")
print("a) Sydney\nb) Melbourne\nc) Canberra\nd) Brisbane")
answer = input("Your answer: ").lower()
if answer == "c" or answer == "canberra":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Canberra")
print("What is the capital of Canada? ")
print("a) Toronto\nb) Vancouver\nc) Ottawa\nd) Montreal")
answer = input("Your answer: ").lower()
if answer == "c" or answer == "ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect! the correct answer is Ottawa")
print("You have completed the quiz! Thank you for playing :)")
print("I hope you enjoyed it!")
print("You got", score, "out of 8 questions correct.")
print("Your score is", (score / 8) * 100,"%")
print("Goodbye!")