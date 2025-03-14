nums = [] #store
# ask for inputs
while True:
    try:
        num = int(input("Enter your number: "))
        nums.append(num) # checks the number
# stops when then input is invalid
    except ValueError:
        break
# print from highest to lowest number