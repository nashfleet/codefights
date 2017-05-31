"""
Looks like your little brother doesn't want to remember the
  multiplication table! Instead he wants to play videogames
  all day long. To teach him a lesson you'd like to write a
  virus that will pop up in the middle of the game and disappear
  only when the brother correctly solves several math questions.

To begin with, you need to construct a multiplication table.
  Given an integer n, return the multiplication table of size n × n.
"""


def multiplicationTable(n):
    return [[(i * j) for i in range(1, n + 1)] for j in range(1, n + 1)]
