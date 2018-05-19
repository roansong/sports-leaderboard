# coding=utf-8
import pytest
from main import parse_line, update_league_data, calculate_standings


@pytest.fixture(scope='module')
def init_league():
    return {
        'Lions': 0,
        'Snakes': 0
    }


@pytest.fixture(scope='module')
def league():
    return {
        'Lions': 5,
        'Snakes': 1,
        'Tarantulas': 6,
        'FC Awesome': 1,
        'Grouches': 0
    }


@pytest.fixture(scope='module')
def leaderboard():
    return {
        5: ['Lions'],
        1: ['FC Awesome', 'Snakes'],
        6: ['Tarantulas'],
        0: ['Grouches']
    }


@pytest.fixture(scope='module')
def scores():
    return [6, 5, 1, 0]


@pytest.mark.usefixtures('init_league')
class TestInput:
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

    def test_league_init(self, init_league):
        league = dict()
        expected = init_league.copy()
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

    def test_score_increment(self, init_league):
        league = init_league.copy()
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


@pytest.mark.usefixtures('league', 'leaderboard', 'scores')
class TestOutput:
    def test_leaderboard_init(self, league):
        leaderboard = dict()
        for team, score in league.items():
            leaderboard[score] = leaderboard.setdefault(score, [])
            leaderboard[score].append(team)
        assert 'FC Awesome' in leaderboard[1]
        assert 'Snakes' in leaderboard[1]

        # introduce some item that does not fit the alphabetical order
        # dict items don't have an order; test could accidentally pass otherwise
        leaderboard[1].append('Apple')

        for score, team in leaderboard.items():
            leaderboard[score] = sorted(leaderboard[score], key=str.lower)

        assert leaderboard[1] == ['Apple', 'FC Awesome', 'Snakes']
        leaderboard[1].pop(0)

    def test_score_sorting(self, leaderboard, scores):
        test_scores = sorted(leaderboard.keys(), reverse=True)
        assert test_scores == scores

    def test_rank_increment(self, leaderboard, league, scores):
        rank = 1
        ranks = []
        scores = scores.copy()
        while rank <= len(league.keys()):
            score = scores.pop(0)
            curr_ranks = [rank] * len(leaderboard[score])
            ranks.extend(curr_ranks)
            rank += len(curr_ranks)
        assert ranks == [1, 2, 3, 3, 5]

    def test_pts_plural(self, scores):
        suffixes = ['s' if score != 1 else '' for score in scores]
        assert suffixes == ['s', 's', '', 's']


class TestAcceptance:
    def test_example_case(self):
        expected_output = (
            '1. Tarantulas, 6 pts\n'
            '2. Lions, 5 pts\n'
            '3. FC Awesome, 1 pt\n'
            '3. Snakes, 1 pt\n'
            '5. Grouches, 0 pts'
        )
        for fname in ['tests/example.txt']:
            update_league_data(fname)
        standings = calculate_standings()
        assert standings == expected_output
