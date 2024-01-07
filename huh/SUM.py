def getSum(n):

    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    return sum


# Driver code
if __name__ == "__main__":
    n = 8169558980

    # Function call
    print(getSum(n))
