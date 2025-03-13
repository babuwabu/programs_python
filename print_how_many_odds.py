# initialize
odds = 0
# input ten numbers
for i in range(10):
    num = int(input(f"Enter number {i +1}: "))
    if num % 2 != 0:
        odds += 1
# print how many odds
print("The total of odd numbers is", odds)