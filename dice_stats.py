import random

# number_count = [1_count, 2_count,..., n_count]

def roll_dice(n, x):
    number_count = {}
    for i in range(1, n + 1):
        number_count.update({f"{i}_count": 0})
    for i in range(1, x + 1):
        roll = random.randint(1, n)
        number_count.update({f"{roll}_count": number_count.get(f"{roll}_count") + 1})
    
    for i, num in enumerate(number_count):
        print(f"[{i + 1}] - {number_count[num]}/{x} -> {round(number_count[num] / x * 100, 2)}%")

if __name__ == "__main__":
    ord = int(input("Please provide an order for the dice: "))
    rolls = int(input("How many times do you want to roll the dice: "))
    roll_dice(ord, rolls)