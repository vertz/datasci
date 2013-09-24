import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if matrix == "a":
	for k in range(5):
            mr.emit_intermediate((row,k), (col ,val))
    else:
	for k in range(5):
            mr.emit_intermediate((k,col), (row ,val))
    

def reducer(key, list_of_values):
    total = 0
    for i in range(5):
      lst = [v[1] for v in list_of_values if v[0] == i]
      if len(lst) == 2:
         total += lst[0]*lst[1]
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
