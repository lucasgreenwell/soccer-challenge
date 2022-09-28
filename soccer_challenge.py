import click

@click.command()
@click.argument('season', type=click.File('r'))
def calculate_season(season):
    season: str = season.read()
    running_scoreboard: dict = {}
    games = season.split("\n")
    for game in games:
        running_scoreboard = update_score_after_game(game, running_scoreboard)
    calculate_ranking_after_season(running_scoreboard)


# helper method that takes in one game
def update_score_after_game(game: str, running_scoreboard: dict):
    # example input: "Lions 3, Snakes 3"

    # parse everything needed from a game string
    teams_with_scores = game.split(",")
    score_one = teams_with_scores[0][-1]
    team_one = teams_with_scores[0][0:-1].strip()
    score_two = teams_with_scores[1][-1]
    team_two = teams_with_scores[1][0:-1].strip()

    # determine winner and assign season points
    if score_one > score_two:
        points_one = 3
        points_two = 0
    elif score_two > score_one:
        points_one = 0
        points_two = 3
    else:
        points_one = 1
        points_two = 1

    # either update or add the teams and season points to running_scoreboard
    if team_one in running_scoreboard.keys():
        running_scoreboard[team_one] += points_one
    else:
        running_scoreboard[team_one] = points_one
    if team_two in running_scoreboard.keys():
        running_scoreboard[team_two] += points_two
    else:
        running_scoreboard[team_two] = points_two

    return running_scoreboard


def calculate_ranking_after_season(running_scoreboard: dict):
    # extract teams and scores into tuples, it's a bit easier to work with than kv pairs
    team_score_tuples = [(k, v) for k, v in running_scoreboard.items()]

    # sort teams alphabetically and then by score
    team_score_tuples.sort(key=lambda x: x[0])
    team_score_tuples.sort(key=lambda x: x[1], reverse=True)

    # format in expected output
    for i, team_score_tuple in enumerate(team_score_tuples):
        # pluralize points if needed
        points = 'pt' if team_score_tuple[1] == 1 else 'pts'

        # if tied, give same place to both teams
        place = i if team_score_tuples[i][1] == team_score_tuples[i - 1][1] else i + 1
        click.echo(
            f"{place}. {team_score_tuple[0]}, {team_score_tuple[1]} {points}")


if __name__ == '__main__':
    calculate_season()
