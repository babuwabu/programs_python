nums = [] #store
# ask for inputs
while True:
    try:
        num = int(input("Enter your number: "))
        nums.append(num) # checks the number
# stops when then input is invalid
    except ValueError:
        break
# print most number of duplicates
if nums:
    most = max(nums, key=nums.count)
    print("The number with most duplicates is", most)