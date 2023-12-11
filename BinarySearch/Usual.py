arr = [1, 2, 3]

left = 0
right = len(arr)
find = 1


while (left < right):
    mid = (left + right) // 2
    print(left, right)
    if arr[mid] == find:
        print(mid)
        break

    elif arr[mid] < find:
        print('Mid is smaller', mid, arr[mid])
        left = mid + 1

    elif arr[mid] > find:
        print('Mid is greater', mid, arr[mid])
        right = mid - 1
