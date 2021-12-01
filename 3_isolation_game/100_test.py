# Test script made for testing algorithms performance
import main

draws = 0
p1 = 0
p2 = 0

for _ in range(0, 100):
    result = main.main()
    if result == "draw":
        draws += 1
    elif result == "1":
        p1 += 1
    elif result == "2":
        p2 += 1

print("Player 1 won " + str(p1) + " times.")
print("Player 2 won " + str(p2) + " times.")
print("Draws number: " + str(draws))

