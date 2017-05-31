"""
A grand Team Chess Tournament will be held at your University.
  Two teams, smarties and cleveries, will clash to determine
  whose chess skills are better. The teams have the same number
  of members, and the ith member of smarties will play against
  the ith member of cleveries in the ith game for each valid i

Given the names of the players of both smarties and cleveries,
  return the games in the order they will be played.
"""


def chessTeams(smarties, cleveries):
    return list(zip(smarties, cleveries))
