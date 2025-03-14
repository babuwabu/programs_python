nums = [] #store
# ask for inputs
while True:
    try:
        num = int(input("Enter your number: "))
        nums.append(num) # checks the number
# stops when then input is invalid
    except ValueError:
        break
# print the average of all inputs
if nums:
    average = sum(nums) / len(nums)
    print("The average of the numbers is", average)