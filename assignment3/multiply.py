import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value.  

Design a MapReduce algorithm to compute matrix multiplication: A x B

The input to the map function will be matrix row records formatted as lists. 
Each list will have the format [matrix, i, j, value] 
where matrix is a string and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record originates from. 
This field has two possible values:
    ‘a’ indicates that the record is from matrix A
    ‘b’ indicates that the record is from matrix B
    
The output from the reduce function will also be matrix row records formatted as tuples. 
Each tuple will have the format (i, j, value) where each element is an integer.
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
