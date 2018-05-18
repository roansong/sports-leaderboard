# coding=utf-8
from sys import argv

DEFAULT_FILE = 'example.txt'
LEAGUE = dict()


def update_league_data(fname: str):
    with open(fname, 'r') as infile:
        match = infile.readline().rstrip()
        while match:
            match_data = [(team[:team.rfind(' ')], team[team.rfind(' '):])
                          for team in match.split(', ')]
            teams, scores = zip(*match_data)
            scores = tuple(int(score) for score in scores)
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
