import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, 
e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, 
then remove any duplicates generated.

The input is a 2 element list: [sequence id, nucleotides]
sequence id: Unique identifier formatted as a string
nucleotides: Sequence of nucleotides formatted as a string

The output from the reduce function should be the unique trimmed nucleotide strings.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    nucleotide = record[1]
    mr.emit_intermediate(nucleotide[:-10], record[0])

def reducer(key, list_of_values):
    mr.emit(key)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
