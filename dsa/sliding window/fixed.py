nums = [1, 1, 3, 4, 5, 6, 7, 8, 9]



def duplicates(nums, k):
    L = 0
    window = set()

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        
        if nums[R] in window:
            return True
        
        window.add(nums[R])    
        
    return False

print(duplicates(nums, 3))