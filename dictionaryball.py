import json
# This entry imports the track_data.json file
file = open('data_soup.json', 'r')
json_data = json.load(file)

# game_dictionary = [{'home': True, 'team_name': 'Brooklyn Nets', 'colors': ['black', 'white'],
#                             'players': [{
#                                 'name': 'Alan Anderson','number': 0,'shoe': 16, 'points': 22, 'rebounds': 12,
#                                  'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1},
#                                 {'name': 'Reggie Evans','number': 30,'shoe': 14, 'points': 12, 'rebounds': 12,
#                                  'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7},
#                                 {'name': 'Brooke Lopez','number': 11,'shoe': 17, 'points': 17, 'rebounds': 19,
#                                  'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15},
#                                 {'name': 'Mason Plumlee','number': 1,'shoe': 19, 'points': 26, 'rebounds': 12,
#                                  'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5},
#                                 {'name': 'Jason Terry','number': 31,'shoe': 15, 'points': 19, 'rebounds': 2,
#                                  'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}]},
#                    {'away': True, 'team_name': 'Charlotte Hornets', 'colors': ['turquoise', 'black'],
#                             'players': [
#                                 {'name': 'Jeff Ardien','number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1,
#                                  'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
#                                 {'name': 'Bismak Biyombo','number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4,
#                                  'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
#                                 {'name': 'DeSagna Diop','number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12,
#                                  'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
#                                 {'name': 'Ben Gordon','number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3,
#                                  'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
#                                 {'name': 'Brendan Haywood','number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12,
#                                  'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}]}]


# Builds a dictionary-structured variable from a json file
def game_dict():
    teams = []
    for team_as_list in json_data:
        team = {}
        if(team_as_list[0][0] == "Home Team" and team_as_list[0][1]== "True"):
            team["home"] = True
        elif (team_as_list[0][0] == "Away Team" and team_as_list[0][1]== "True"):
            team["away"] = True
        team['team_name'] = team_as_list[1][1]
        team['colors'] = team_as_list[2][1:3]
        team['players'] = []
        for i, player_name in enumerate(team_as_list[3][1:6]):
            player = {}
            player['name'] = player_name
            for j in range(4,12):
                player[team_as_list[j][0].lower().replace(" ", "_")] = int(team_as_list[j][i+1])
            team['players'].append(player)
        teams.append(team)
    return teams

game_dictionary = game_dict()

# Takes in a player name and returns the number of points 
# scored by a given player
def num_points_scored(player_name):
    num_of_points = 0
    for entry in game_dictionary:
        for player in entry["players"]:
                if player["name"] == player_name:
                    num_of_points = player["points"]
    return num_of_points

print(num_points_scored('Brendan Haywood'))

# Takes in a player name and returns the shoe size 
# of a given player
def shoe_size(player_name):
    player_shoe_size = 0
    for entry in game_dictionary:
        for player in entry["players"]:
                if player["name"] == player_name:
                    player_shoe_size = player["shoe"]
    return player_shoe_size

print(shoe_size('Brendan Haywood'))

# Takes in a team name and returns the colors of the team
def team_colors(team_name):
    team_colors = None
    for entry in game_dictionary:
        if entry["team_name"] == team_name:
            team_colors = (entry["colors"])
    return team_colors

print(team_colors("Charlotte Hornets"))

# Returns the team names found in game_dictionary
def team_names():
    list_of_entries_found = []
    for entry in game_dictionary:
        list_of_entries_found.append(entry["team_name"])
    return list_of_entries_found

print(team_names())

# Takes in a team name and returns the players'
# shirt numbers
def player_numbers(team_name):
    list_of_entries_found = []
    for entry in game_dictionary:
        if entry["team_name"] == team_name:
            for player in entry["players"]:
                    list_of_entries_found.append(player["number"])
    return list_of_entries_found

print(player_numbers("Brooklyn Nets"))

# Takes in a player name and returns the specified
# player's stats
def player_stats(player_name):
    player_dictionary = {}
    for entry in game_dictionary:
        for player in entry["players"]:
            if player["name"] == player_name:
                player_dictionary["Number"] = player["number"]
                player_dictionary["Shoe"] = player["shoe"]
                player_dictionary["Points"] = player["points"]
                player_dictionary["Rebounds"] = player["rebounds"]
                player_dictionary["Assists"] = player["assists"]
                player_dictionary["Steals"] = player["steals"]
                player_dictionary["Blocks"] = player["blocks"]
                player_dictionary["Slam_Dunks"] = player["slam_dunks"]
    return player_dictionary

print(player_stats("Alan Anderson"))

# Return the number of rebounds associated with 
# the player that has the largest shoe size.
def big_shoe_rebounds():
    largest_shoe_size = 0
    number_of_rebounds = 0
    for entry in game_dictionary:
        for player in entry["players"]:
            if player["shoe"] > largest_shoe_size:
                largest_shoe_size = player["shoe"]
                number_of_rebounds = player["rebounds"]
                player_name = player["name"]
    return f"{player_name}'s shoe size is: {largest_shoe_size}, and his number of rebounds is {number_of_rebounds}"

print(big_shoe_rebounds())

# Answers the questions: Which player has the most points?
def most_points_scored():
    highest_point_count = 0
    player_name = None
    for entry in game_dictionary:
        for player in entry["players"]: 
            if player["points"] > highest_point_count:    
                highest_point_count = player["points"]
                player_name = player["name"]
    return player_name

print(most_points_scored())

# Answers the questions: Which team has the most points?
def team_points(team_name):
    all_player_points = 0
    for entry in game_dictionary:
        if entry["team_name"] == team_name:
            for player in entry["players"]:
                player_points = num_points_scored(player["name"])
                all_player_points = all_player_points + player_points
    return all_player_points

print(team_points("Brooklyn Nets"))

# Answers the questions: Which one is the winning team?
def winning_team():
    brooklyn_nets_points = team_points("Brooklyn Nets")
    charlotte_hornets_points = team_points("Charlotte Hornets")
    if brooklyn_nets_points > charlotte_hornets_points:
        return "Brooklyn Nets"
    if brooklyn_nets_points < charlotte_hornets_points:
        return "Charlotte Hornets"
    else:
        return "It's a tie!"

print(winning_team())

# Answers the question: What's the player with the longest name?
def player_with_longest_name():
    longest_name = None
    name_counter = 0
    for entry in game_dictionary:
        for player in entry["players"]:
           if len(player["name"]) > name_counter:
               name_counter = len(player["name"])
               longest_name = player["name"]
    return longest_name

print(player_with_longest_name())

# Returns true if the player with the longest name 
# had the most steals.
def long_name_steals_a_ton():
    longest_name = player_with_longest_name()
    counter = 0
    most_steals = None
    for entry in game_dictionary:
        for player in entry["players"]:
           if player["steals"] >  counter:
               counter = player["steals"]
               most_steals = player["name"]
    if most_steals == longest_name:
        return True
    else:
        return False

print(long_name_steals_a_ton())
