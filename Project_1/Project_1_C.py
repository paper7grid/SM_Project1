print("Hello Welcome to my World Quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
answer = input("What is the capital of India? ").lower()
if answer == "delhi":
    print("Correct!")
else: 
    print("Incorrect! the correct answer is Delhi")
answer == input("What is the capital of USA? ").lower()
if answer == "washington d.c.":
    print("Correct!")
else: 
    print("Incorrect! the correct answer is Washington D.C.")
answer = input("What is the capital of Japan? ").lower()
if answer == "tokyo":
    print("Correct!")
else:
    print("Incorrect! the correct answer is Tokyo")
answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print("Correct!")
else:
    print("Incorrect! the correct answer is Paris")
print("You have completed the quiz! Thank you for playing :)")
# End of Project_1_C.py