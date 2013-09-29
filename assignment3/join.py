import MapReduce
import sys

"""
Implement a relational join as a MapReduce query

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id

MapReduce query should produce the same information as this SQL query.  

consider the two input tables, Order and LineItem, as one big concatenated bag of records 
which gets fed into the map function record by record

The input will be database records formatted as lists of Strings.

Every list element corresponds to a different field in it’s corresponding record.
The first item(index 0) in each record is a string that identifies which table the record originates from. 
This field has two possible values:

   ‘line_item’ indicates that the record is a line item.
   ‘order’ indicates that the record is an order.

The second element(index 1) in each record is the order_id.

The output should be a joined record.
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
