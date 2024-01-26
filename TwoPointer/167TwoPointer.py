numbers = [1, 2, 7, 11, 18, 20]
target = 27
left = 0
right = len(numbers) - 1
sum = 0
while left < right:
    print(left, right)
    sum = numbers[left] + numbers[right]

        
    if sum > target:
        right -= 1
        
    elif sum < target:
        left += 1

    else:
        print([left, right])  
        break      

