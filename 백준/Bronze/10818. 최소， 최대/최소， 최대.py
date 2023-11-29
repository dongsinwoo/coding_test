n = int(input(""))
nums = list(map(int, input("").split(" ")))
nums.sort()
print(f"{nums[0]} {nums[n-1]}")