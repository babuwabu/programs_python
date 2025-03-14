# ask for ten numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
# checking if the numbers are duplicated
for num in nums:
    if nums.count(num) == 1:
        print(num) # print the numbers that has no duplicate