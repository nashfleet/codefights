"""
There are some students standing in a row, each has some number written
 on their back. The students are about to divide into two teams by
 counting off by twos: those standing at the even positions (0-based)
 will go to team A, and those standing at the odd position will join
 the team B.

Your task is to calculate the difference between the sums of numbers
  written on the backs of the students that will join team A, and those
  written on the backs of the students that will join team B.
"""
def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])
