from bisect import bisect_left, bisect, bisect_right

arr = [2, 3, 5, 4, 6, 2, 1, 4, 5, 7, 7, 7, 7, 9, 9]

left = 0
right = len(arr)
find = 7

while left < right:

    # mid = left + (right - left) // 2
    mid = (left + right) // 2

    if arr[mid] < find:
        left = mid + 1

    if arr[mid] > find:
        right = mid

    else:
        print(left)
        break
