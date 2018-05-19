# Sports Leaderboard [![Build Status](https://travis-ci.org/roansong/sports-leaderboard.svg?branch=master)](https://travis-ci.org/roansong/sports-leaderboard)


## Getting Started

1. Create a python3 virtual environment and install project requirements, either
   by running 
   
   ``make venv`` 
   
   or doing it manually with 

   ```
   python3 -m venv venv
   venv/bin/pip install -r requirements.txt
   ```

2. Run tests:

    ``make test``    

3. Run the example code by calling 
    
   ``make`` or ``make example``
    
   You can specify files to load by calling
   
   ``./main file1 file2 ... fileN``
   
   or

   ``venv/bin/python main.py file1 file2 ... fileN``
    
   If no arguments are given, the default file will be used (``example.txt``).
   Output is saved to a timestamped text file in the ``data`` folder.
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

e.g. the above input should produce the following output:

```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```
