# ask ten numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
# check numbers and if the number is duplicated
seen = set()
for num in nums:
    if nums.count(num) > 1 and num not in seen:
        print(num) # print the duplicated numbers
        seen.add(num)
