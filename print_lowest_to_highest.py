nums = [] #store
# ask for inputs
while True:
    try:
        num = int(input("Enter your number: "))
        nums.append(num) # checks the number
# stops when then input is invalid
    except ValueError:
        break
# print lowest to higher number from user inputs
if nums:
    nums.sort()
    print("The numbers from lowest to highest numbers are", nums)