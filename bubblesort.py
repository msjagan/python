
nums = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(nums)

# Method 1
# for x in range(0,len(nums)):
# 	for y in range(len(nums)):
# 		if nums[x] < nums[y]:
# 			nums[x], nums[y] = nums[y], nums[x]
# print(nums)

# Actual Bubble Sort
for x in range(0, len(nums)):
	for y in range(x+1, len(nums)):
		if nums[y] < nums[x]:
			nums[x], nums[y] = nums[y], nums[x]
		print(x, y)
print(nums)