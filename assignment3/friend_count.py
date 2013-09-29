import MapReduce
import sys

"""
Consider a simple social network dataset consisting of key-value pairs 
where each key is a person and each value is a friend of that person. 
Describe a MapReduce algorithm to count he number of friends each person has

The input is a 2 element list: [personA, personB]
personA: Name of a person formatted as a string
personB: Name of one of personA’s friends formatted as a string
This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB.

The output should be a (person,  friend count) tuple.
person is a string and friend count is an integer describing the number of friends ‘person’ has.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[0], 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
