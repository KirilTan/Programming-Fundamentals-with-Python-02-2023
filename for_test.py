def tribonacci(n):
    sequence = [1, 1, 2]

    for i in range(3, n):
        next_term = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_term)

    print(*sequence[:n])

# Take user input for the number of terms
n = int(input("Enter the number of Tribonacci terms: "))
tribonacci(n)
