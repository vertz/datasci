import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
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
