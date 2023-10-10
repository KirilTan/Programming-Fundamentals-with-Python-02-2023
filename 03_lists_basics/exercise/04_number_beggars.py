# Input
money_pool = [int(s) for s in input().split(", ")]
number_of_beggars = int(input())

# Calculations
final_cuts = []

for beggar in range(number_of_beggars):

    current_beggar_cut = 0

    for i in range(beggar, len(money_pool), number_of_beggars):
        current_beggar_cut += money_pool[i]

    final_cuts.append(current_beggar_cut)

print(final_cuts)
