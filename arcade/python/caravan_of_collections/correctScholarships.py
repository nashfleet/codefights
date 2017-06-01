"""
For the upcoming academic year the Coolcoders University should
  decide which students will get the scholarships. Scholarships
  are considered to be correctly distributed if all best students
  have it, but not all students in the university do. Obviously,
  only university students should be able to get a scholarship,
  i.e. there should be no outsiders in the list of the students
  that will get a scholarships.

You are given lists of unique student ids bestStudents, scholarships
  and allStudents, representing ids of the best students, students
  that will get a scholarship and all the students in the university,
  respectively. Return true if the scholarships are correctly
  distributed and false otherwise.
"""


def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)
