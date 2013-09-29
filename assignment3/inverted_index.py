import MapReduce
import sys

"""
Create an Inverted index. 

Given a set of documents, an inverted index is a dictionary 
where each word is associated with a list of the document identifiers in which that word appears.  

The input is a 2 element list: [document_id, text]
document_id: document identifier formatted as a string
text: text of the document formatted as a string

The output should be a (word, document ID list) tuple 
where word is a String and document ID list is a list of Strings.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents word occurrence in
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
