"""
John has just entered a college, and should now pick several courses
  to take. He knows nothing, except that number x is a bad luck for
  him, which is why he won't even consider courses whose title
  consist of x letters.

Given a list of courses, remove the courses with titles consisting
  of x letters and return the result.
"""


def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))
