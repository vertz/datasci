import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.

The input is a 2 element list: [personA, personB]
personA: Name of a person formatted as a string
personB: Name of one of personA’s friends formatted as a string
This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB.

The output should be the (person, friend) and (friend, person) tuples for each asymmetric friendship.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, (personA, personB))
    mr.emit_intermediate(personB, (personA, personB))

def reducer(key, list_of_values):
    self_list    = [v for v in list_of_values if v[0] == key]
    others_list  = [v for v in list_of_values if v[1] == key]
    for v1 in self_list:
      nm = False
      if (v1[1], v1[0]) not in others_list:
         mr.emit((v1[0], v1[1]))
	 mr.emit((v1[1], v1[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
