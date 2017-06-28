"""
Billy and Mandy are twins, and as such they do everything together.
  Unfortunately during the finals they were forced to write their
  exams separately, which explains why they got such low scores.
  However, they are not too sad about it: since they are twins, it's
  only natural for them to work together, so they are going to sum
  up their scores for each exam and show them to their mom.

Given two lists of equal size representing the scores Billy and
  Mandy got for each exam (b and m, respectively), return a single
  list containing their combined score.
"""


def twinsScore(b, m):
    return list(map(sum, zip(b, m)))
