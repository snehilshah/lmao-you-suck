sum = 0
sum_cube = 0
max_red, max_green, max_blue = 0, 0, 0
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}
dump = []

with open('./AdventOfCode/Day2/input.txt') as file:
    for line in file:
        max_red, max_green, max_blue = 0, 0, 0
        flag = True

        game, data = line.split(":")
        game = game.split(" ")
        game_num = int(game[1])
        # print(game_num)

        mini_game = data.split(";")
        # print(mini_game)

        for values in mini_game:
            pair = [c.strip() for c in values.split(",")]
            # print(pair)

            for some in pair:

                num, color = some.split(" ")
                color = color.strip()
                if color == "red":
                    max_red = max(int(num), max_red)
                elif color == "green":
                    max_green = max(int(num), max_green)
                elif color == "blue":
                    max_blue = max(int(num), max_blue)

                if limits[color] < int(num):
                    flag = False
                    # can break in part 1 
                    # required to check all the values in part 2 hence removing the break
                    # break

        sum_cube += max_red * max_green * max_blue
        if flag:
            sum += game_num

print(sum)
print(sum_cube)
