game_config = {
    "blue": 14,
    "red": 12,
    "green": 13,
}


with open('in.txt', 'r') as f:
    games = {}
    for line in f.readlines():
        game_num, config = line.split(":")
        
        game_num = int(game_num.split(" ")[-1])

        # convert sets to one game, and take max later
        config = config.replace(";", ",").split(",")

        games[game_num] = {
            "blue": 0,
            "red": 0,
            "green": 0,
        }

        for color in config:
            count, clr = color.strip().split(" ")

            # take max of each color
            games[game_num][clr] = max(int(count), games[game_num][clr])
    

    possible_games = []
    for id, game in games.items():
        if game['red'] <= game_config['red'] \
        and game['blue'] <= game_config['blue'] \
        and game['green'] <= game_config['green']:
            possible_games.append(id)
        


    print(sum(possible_games))