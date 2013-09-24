import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    order_list = [record for record in list_of_values if record[0] == "order"]
    line_list  = [record for record in list_of_values if record[0] == "line_item"]
    lst = []
    for order_item in order_list:
      for line_item in line_list:
	  record = list(order_item)
	  record.extend(line_item)
	  lst.append(record)

    for item in lst:
	mr.emit(item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
