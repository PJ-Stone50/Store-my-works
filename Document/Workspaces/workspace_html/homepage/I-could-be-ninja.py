import statistics
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# print(findDuplicate([2,1,3,4,2,6,2,1,6,4,6,7,6]))
# print("="*30)
print(statistics.median([1,2,3,2,2,5,6]))
