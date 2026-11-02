# 40th github project --> Higher or Lower
print('----------Higher or Lower----------')
import random


def main():
    print("HIGHER OR LOWER")
    print("Guess if the next number is higher or lower.")

    current = random.randint(1, 100)
    score = 0

    while True:
        print(f"\nCurrent number: {current}")
        guess = input("Higher or lower? (h/l): ").strip().lower()

        if guess not in ("h", "l"):
            print("Enter 'h' or 'l'.")
            continue

        next_num = random.randint(1, 100)
        print(f"Next number: {next_num}")

        if next_num == current:
            print("Same number! No change to score.")
        elif (guess == "h" and next_num > current) or (guess == "l" and next_num < current):
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Final score: {score}")
            break

        current = next_num



main()