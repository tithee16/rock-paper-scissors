import random

choices = {
    1: '✊',
    2: '✋',
    3: '✌️'
}

print("=====================")
print(" Rock Paper Scissors ")
print("=====================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player_input = input("Pick a number: ")

if player_input.isdigit():
    player = int(player_input)
    if player < 1 or player > 3:
        print("Invalid input! Please choose a number between 1 and 3.")
        exit()
else: 
    print("Invalid input! Please enter a number.")
    exit()

computer = random.randint(1,3)

print(f"\n Player choose: {choices[player]}")
print(f"\n Computer chose: {choices[computer]}")

if player == computer:
     print("It's a tie!")
elif(
     (player == 1 and computer == 3) or
     (player == 2 and computer == 1) or
     (player == 3 and computer == 2)
):
     print("The player won!")
else:
     print("The Computer won!")