nums = [] # store
# ask user inputs and loop for the user to input continously until invalid
while True:
    try:
        num = int(input("Enter your number: "))
        if num in nums: # checks number if duplicate
            print("Duplicate") # if true print duplicate
        else: # checks number if unique
            print ("Unique") # if true print unique
            nums.append(num)
# stop the input when invalid
    except ValueError:
        break 