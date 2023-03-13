import random

computer_number = random.randint(10,40)

pos = True
guess_number = 0

while pos==True :
    user_number = int(input("Guess your number Between 10 and 40 :"))
    if user_number == computer_number :
        guess_number = guess_number + 1
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉 Y o u W i n !! 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print("You win after",guess_number,"guess")
        break

    elif user_number < computer_number :
        guess_number = guess_number + 1
        print("go up")
    
    elif user_number > computer_number :
        guess_number = guess_number + 1
        print("go down")
