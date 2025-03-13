# initialize the total
total = 0
# input ten numbers and calculate the sum of all numbers
for i in range(10):
    num = int(input(f"Enter number {i +1}: "))
    total += num
# print the sum
print("The sum of all ten numbers is", total)