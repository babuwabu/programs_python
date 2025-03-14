# initialize number of even numbers
evens = 0
# ask to input 10 numbers and calculate how many are the even numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        evens += 1
# print the number of evens