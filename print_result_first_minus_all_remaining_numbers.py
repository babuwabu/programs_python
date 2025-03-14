# ask to input 10 numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
# calculate the result
result = nums[0] - sum(nums[1:])
# print the result of the first number minus all the remaining numbers
print("The result of the first number minus all the remaining numbers", result)