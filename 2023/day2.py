from pathlib import Path

games = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

games = Path("2023/day2.txt").read_text().splitlines()


# part 1
# 12 red, 13 green, 14 blue
# ignore games with any value exceeding this
def is_valid_game(game: str) -> bool:
    draws = game.split(": ", maxsplit=1)[1].split("; ")
    for draw in draws:
        for colour_draw in draw.split(", "):
            n_str, colour = colour_draw.split(" ")
            n = int(n_str)
            if colour == "red" and n > 12:
                return False
            elif colour == "green" and n > 13:
                return False
            elif colour == "blue" and n > 14:
                return False
    return True


valid_game_sum = 0
for i, game in enumerate(games, start=1):
    if is_valid_game(game):
        valid_game_sum += i

print(valid_game_sum)


# part 2
def game_power(game: str) -> int:
    max_vals = {"red": 0, "green": 0, "blue": 0}
    draws = game.split(": ", maxsplit=1)[1].split("; ")
    for draw in draws:
        for colour_draw in draw.split(", "):
            n_str, colour = colour_draw.split(" ")
            n = int(n_str)
            max_vals[colour] = max(max_vals[colour], n)
    return max_vals["red"] * max_vals["green"] * max_vals["blue"]


power = 0
for game in games:
    power += game_power(game)

print(power)
