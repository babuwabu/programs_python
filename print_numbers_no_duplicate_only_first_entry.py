# ask for ten numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
seen = set() # keeps the numbers that could be duplicated
# checks the number if it's duplicate and keep the first entry
for num in nums:
    if num not in seen:
        print(num) # print those numbers
        seen.add(num) # mark numbers seen