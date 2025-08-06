import random

def main():
    roll_again()

def order():
    return int(input("Enter the order of the dice: D"))
    

def roll_again():
    roll = input("Do you want to roll the dice? (y/n): ").strip().lower()
    if roll == 'y':
        roll_dice(order())
    elif roll == 'n':
        print("See you soon!")
    else: 
        print("Wrong input, please type 'y' or 'n'")
        roll_again()

def roll_dice(order):
    result = random.randint(1, order)
    print("The dice rolled a", str(result))
    roll_again()
    

main()