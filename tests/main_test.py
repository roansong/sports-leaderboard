# coding=utf-8
from main import parse_line


class TestInput(object):
    def test_parse_line(self):
        match = 'Lions 3, Snakes 3'
        teams, scores = parse_line(match)
        assert teams, scores == (('Lions', 'Snakes'), (3, 3))

    def test_parse_line_2(self):
        match = 'Lions With Spaces 3, FC weird-format 3'
        teams, scores = parse_line(match)
        assert teams, scores == (
            ('Lions With Spaces', 'FC weird-format'), (3, 3)
        )

    def test_league_init(self):
        league = dict()
        expected = {
            'Lions': 0,
            'Snakes': 0
        }
        teams = ('Lions', 'Snakes')
        [league.setdefault(team, 0) for team in teams]
        assert league == expected

    def test_adding_to_league(self):
        league = {
            'Lions': 1,
            'Snakes': 1
        }
        expected = {
            'Lions': 1,
            'Snakes': 1,
            'New Team': 0
        }
        teams = ('Lions', 'New Team')
        [league.setdefault(team, 0) for team in teams]
        assert league == expected

    def test_score_increment(self):
        league = {
            'Lions': 0,
            'Snakes': 0
        }
        teams = ('Lions', 'Snakes')
        scores = (3, 3)

        if scores[0] == scores[1]:
            league[teams[0]] += 1
            league[teams[1]] += 1

        assert league['Lions'] == 1
        assert league['Snakes'] == 1

        teams = ('Lions', 'Snakes')
        scores = (3, 1)

        if scores[0] > scores[1]:
            league[teams[0]] += 3
        else:
            league[teams[1]] += 3

        assert league['Lions'] == 4
        assert league['Snakes'] == 1


class TestOutput(object):
    pass
