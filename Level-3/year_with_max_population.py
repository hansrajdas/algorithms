#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# List of person with their birth and death years are given. Find the year with
# highest population.
#
# Approach:
# 1. Initialize a list of size last birth - first birth + 1.
# 2. Increment value at year index if there is a birth, decrement value at year
# index if there is a death(ignore if death year lies after last birth year as
# this can't be year with max population).
# 3. Scan list to find year having max population.
#
# Explained here - https://vimeo.com/158532188
#
# Complexity:
# O(Y + P) where
# Y = range of birth years(last birth - first birth)
# P = Number of person


import collections


Person = collections.namedtuple('Person', ['name', 'birth', 'death'])


def get_first_and_last_birth_years(persons):
  """
  Finds first and last birth years from list births and deaths.

  Args:
    persons: List of person with name, birth and death year.

  Returns: Dictionary with first and last birth years.
  """
  birth_years = {'first': persons[0].birth, 'last': persons[0].birth}
  for person in persons:
    if person.birth < birth_years['first']:
      birth_years['first'] = person.birth

    if person.birth > birth_years['last']:
      birth_years['last'] = person.birth

  return birth_years


def get_year_with_population(persons):
  """
  Finds year with max population.

  Args:
    persons: List of person with name, birth and death year.

  Returns: Year with max population.
  """
  birth_years = get_first_and_last_birth_years(persons)
  first_birth = birth_years['first']
  last_birth = birth_years['last']
  birth_death_years = [0 for i in range(last_birth - first_birth + 1)]

  # Populate 'birth_death_years' list to have +1 when there is a birth and -1
  # when there is a death in a year.
  for person in persons:  # O(P)
    birth_death_years[person.birth - first_birth] += 1

    # If persons death year is more than last birth year, no need to track for
    # that as those years can't be year with max population.
    if len(birth_death_years) > person.death - first_birth + 2:
      birth_death_years[person.death - first_birth + 1] -= 1

  max_population_year = 0
  person_count = 0
  for year in range(len(birth_death_years)):  # O(Y)
    if person_count < person_count + birth_death_years[year]:
      person_count += birth_death_years[year]
      max_population_year = year

  return max_population_year + first_birth


def main():
  persons = [
    Person('P1', 2001, 2005),
    Person('P2', 2005, 2009),
    Person('P3', 2003, 2020),
    Person('P3', 2002, 2002),
  ]
  print ('Year with max population is: %d' % get_year_with_population(persons))


if __name__ == '__main__':
  main()


# Output:
# ---------------------------------
# Year with max population is: 2005
