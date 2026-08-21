def armstrong(n, m):
    for i in range(n, m + 1):
        count = 0
        temp = i

        while temp > 0:
            temp //= 10
            count += 1

        k = i
        j = k
        arms = 0

        while k > 0:
            digit = k % 10
            arms += digit ** count
            k //= 10

        if arms == j:
            print(j, "is an Armstrong number")

armstrong(1, 100)