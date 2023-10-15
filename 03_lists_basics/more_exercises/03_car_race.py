# Input
racers_and_finish_line = input().split()

# Split the racers
left_racer = racers_and_finish_line[:len(racers_and_finish_line) // 2]
right_racer = racers_and_finish_line[len(racers_and_finish_line) - 1: len(racers_and_finish_line) // 2: -1]


# Calculate total time for each racer
def calculate_total_time(racer):
    total_time = 0
    for current_time in racer:
        current_time = int(current_time)
        total_time = (total_time * 0.8) if current_time == 0 else (total_time + current_time)
    return total_time


# Calculate total time for left and right racers
left_racer_time, right_racer_time = calculate_total_time(left_racer), calculate_total_time(right_racer)

# Output
winner = "left" if left_racer_time < right_racer_time else "right"
print(f"The winner is {winner} with total time: {left_racer_time if winner == 'left' else right_racer_time:.1f}")

