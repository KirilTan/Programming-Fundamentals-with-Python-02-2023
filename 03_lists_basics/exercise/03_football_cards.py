start_team_a = ["A-" + str(s) for s in range(1, 12)]
start_team_b = ["B-" + str(s) for s in range(1, 12)]

finish_team_a = start_team_a.copy()
finish_team_b = start_team_b.copy()


players_with_red_card = input().split(" ")

game_terminated = False
for current_player in players_with_red_card:
    if current_player in finish_team_a:
        finish_team_a.remove(current_player)
    elif current_player in finish_team_b:
        finish_team_b.remove(current_player)

    if len(finish_team_a) < 7 or len(finish_team_b) < 7:
        game_terminated = True
        break

print(f"Team A - {len(finish_team_a)}; Team B - {len(finish_team_b)}")
if game_terminated:
    print("Game was terminated")
