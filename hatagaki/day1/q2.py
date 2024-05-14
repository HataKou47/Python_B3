import sys

args = sys.argv

nums = list(map(int, args[1:]))

print(nums[0] + nums[1] + nums[2], end = "")