current_version = [int(number) for number in input().split(".")]
# Note: there will be no case in which the first number will become greater than 9.

current_version[2] += 1
if current_version[2] > 9:
    current_version[2] = 0
    current_version[1] += 1

if current_version[1] > 9:
    current_version[1] = 0
    current_version[0] += 1

print(*current_version, sep=".")
