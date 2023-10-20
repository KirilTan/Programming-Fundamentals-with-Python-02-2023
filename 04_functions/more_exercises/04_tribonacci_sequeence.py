def tribonacci_sequence(n: int) -> list:
    sequence = [1, 1, 2]

    for i in range(3, n):
        next_term = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_term)

    return sequence


# Take user input for the number of terms
num = int(input())
output_text = tribonacci_sequence(num)
print(*output_text[:num])
