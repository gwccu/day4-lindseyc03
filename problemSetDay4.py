# file name: problemSetDay4.py
# guessing
mysteryNum = 3
player = int(input("Guess a number: "))
while (player != mysteryNum):
    player = int(input("Try again:"))
print("You have guessed the magic number!")

# strength
strength = 5
print('Your current strength is:', strength)

while strength <= 10:
    print('Your current strength is:', strength)
    strength += 1
print('You have grown stronger, you can now move on to the next level.')

# n to power of m
n = 2
m = 3
counter = 1
n**m
print("n raised to the power of m is:", n**m)
while(counter != m):
    n *= 2
    counter += 1

print('n raised to the power of m is: ', n)
