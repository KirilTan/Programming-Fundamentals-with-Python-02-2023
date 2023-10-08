# Input
num = int(input())

# Check if number is prime
is_prime = True  # assume the number is prime initially

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

# Output
if is_prime and num > 1:
    print("True")  # num is prime
else:
    print("False")  # num is not prime
