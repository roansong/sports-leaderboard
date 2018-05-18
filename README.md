# Sports 'n' Stuff

## Getting Started

1. Create a python3 virtual environment: 

   ``python3 -m venv venv``
   
2. Install project requirements:

    ``venv/bin/pip install -r requirements.txt``
    
3. Run!

    ``venv/bin/python file1 file2 ... fileN``
    
    If no arguments are given, the default file will be used (``example.txt``).
    
## File Format

The input files should contain a sequence of matches, one per line. The format
should be 

``Team1 Score1, Team2 Score2``

e.g.

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

## League Ranking

For each match, scores are compared and teams' league rankings are updated.
A win is worth 3 points, a draw is worth 1 point, and a loss is worth 0 points.
In the case where one or more teams share a league score, they are given the
same rank and are ordered alphabetically.

e.g. the above input should output:

```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```
