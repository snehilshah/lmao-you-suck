def is_armstrong_number(num):
    # Calculate the number of digits in the number
    num_of_digits = len(str(num))
    
    # Calculate the sum of the cubes of each digit
    sum_of_cubes = sum(int(digit) ** num_of_digits for digit in str(num))
    
    # Check if the number is an Armstrong number
    if sum_of_cubes == num:
        return True
    else:
        return False

count = 0
num = 0

while count < 10:
    num += 1
    if is_armstrong_number(num):
        print(num)
        count += 1