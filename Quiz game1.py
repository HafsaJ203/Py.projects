print("Welcome to my computer! ")

playing = input("Do you want to play a game? ")

if playing.lower() != 'yes':
    quit()

print("OK! Let's play:)")

score = 0

#1
answer = input('What does CPU stand for? ')

if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#2
answer = input('Whose nose grew longer every time he lied? ')

if answer.lower() == 'pinocchio':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#3
while True:
    try:
        answer = int(input('How many equal sides does an isosceles triangle have? '))
            
        if answer == 2:
            print("Correct!")
            score += 1
            break

        elif answer != 2:
            print("Incorrect! It's 2:(")
            break

    except ValueError:
            print("Input is not an integar:/ ")


#4
answer = input('Who discovered electricity? ')

if answer.lower() == 'benjamin franklin':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#5
while True:
    try:
        answer = int(input('How many cards are there in a complete pack of cards? '))
        
        if answer == 52:
            print("Correct!")
            score += 1
            break

        elif answer != 52:
            print("Incorrect! It is 52:(")
            break

    except ValueError:
        print("Input not an integer:/ ")

print(f'You got {score}/5 points!')
