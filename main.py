# coding=utf-8
import datetime
from sys import argv
from typing import List, Tuple

DEFAULT_FILE = 'tests/example.txt'
LEAGUE = dict()
DATA_DIR = 'data'


def parse_line(line: str) -> Tuple[Tuple[str], Tuple[int]]:
    """
    This function accepts a line containing match data, and returns the teams
    and scores of the match.

    Note: to account for team names with spaces, the last space on each side is
    used as the index at which to split between team and score.

    Example input::

        'Lions 3, FC Awesome 4'

    Example output::

        (('Lions', 'FC Awesome'), (3, 4))

    :param line: String describing a single match, e.g.
           ``'Lions 3, FC Awesome 4'``
    :return: Tuple containing a tuple of team names and a tuple of scores
    """
    match_data = [(team[:team.rfind(' ')], team[team.rfind(' '):])
                  for team in line.split(', ')]
    teams, scores = zip(*match_data)
    scores = tuple(int(score) for score in scores)
    return teams, scores


def update_league_data(fname: str) -> None:
    """
    This function reads match data from the file specified by ``fname`` and
    updates the global ``LEAGUE`` dictionary with match results. Dictionaries
    are mutable objects, so no value is returned from this function.

    Scoring:

    ======  ======
    Result  Points
    ======  ======
    Win     3
    Draw    1
    Loss    0
    ======  ======

    :param fname: String filename
    :return: None
    """
    with open(fname, 'r') as infile:
        match = infile.readline().rstrip()
        while match:
            teams, scores = parse_line(match)
            [LEAGUE.setdefault(team, 0) for team in teams]
            if scores[0] == scores[1]:
                LEAGUE[teams[0]] += 1
                LEAGUE[teams[1]] += 1
            elif scores[0] > scores[1]:
                LEAGUE[teams[0]] += 3
            else:
                LEAGUE[teams[1]] += 3
            match = infile.readline().rstrip()


def calculate_standings() -> str:
    """
    This function generates a leaderboard from the global ``LEAGUE`` dictionary.
    Teams are ranked by their score in descending order. Any teams with the same
    score are given a matching rank, and are ordered alphabetically.

    Example output::

        1. Tarantulas, 6 pts
        2. Lions, 5 pts
        3. FC Awesome, 1 pt
        3. Snakes, 1 pt
        5. Grouches, 0 pts

    :return: A string displaying the leaderboard
    """
    leaderboard = dict()
    for team, score in LEAGUE.items():
        leaderboard[score] = leaderboard.setdefault(score, [])
        leaderboard[score].append(team)
    for score, team in leaderboard.items():
        leaderboard[score] = sorted(leaderboard[score], key=str.lower)
    scores = sorted(leaderboard.keys(), reverse=True)
    output_lst = []
    rank = 1
    while rank <= len(LEAGUE.keys()):
        score = scores.pop(0)
        suffix = 's' if score != 1 else ''
        output = [f'{rank}. {team}, {score} pt{suffix}'
                  for team in leaderboard[score]]

        output_lst.extend(output)
        rank += len(output)
    return '\n'.join(output_lst)


if __name__ == '__main__':
    if len(argv) > 1:
        fnames = argv[1:]
    else:
        fnames = [DEFAULT_FILE]
    print(f'Reading from files: {", ".join(fnames)}')

    for fname in fnames:
        update_league_data(fname)

    standings = calculate_standings()
    print(standings)

    timestamp = datetime.datetime.now()
    outfile_name = f'standings_{timestamp:%y-%m-%dT%H-%M-%S}.txt'
    with open(f'{DATA_DIR}/{outfile_name}', 'w') as outfile:
        outfile.write(standings + '\n')
