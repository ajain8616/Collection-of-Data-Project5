import pandas as pd
inventory = [
    {"style": "A", "composition" : [ 
        {"color" : "black" , "size": [{"size":"S" , "qty" : 10},
                                    {"size":"M" , "qty" : 19},
                                    {"size":"L" , "qty" : 25}]},
        {"color" : "blue" , "size": [{"size":"S" , "qty" : 10},
                                    {"size":"M" , "qty" : 19},
                                    {"size":"L" , "qty" : 25}]}
        ] }, 
     {"style": "B", "composition": [ 
        {"color" : "grey" , "size": [{"size":"S" , "qty" : 10},
                                    {"size":"M" , "qty" : 20},
                                    {"size":"L" , "qty" : 45},
                                    {"size":"xL" , "qty" : 25},
                                    {"size":"xxL" , "qty" : 60}]},
         {"color" : "green" , "size": [{"size":"S" , "qty" : 10},
                                    {"size":"M" , "qty" : 20},
                                    {"size":"L" , "qty" : 45},
                                    {"size":"xL" , "qty" : 25},
                                    {"size":"xxL" , "qty" : 60}]}
        ] },
      {"style": "C", "composition": [
      {"color" : "azure" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"xl" , "qty" :58},
                                    {"size":"xxL" , "qty" : 30}]},
      {"color" : "yellow" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"xl" , "qty" :58},
                                    {"size":"xxL" , "qty" : 30}]},
      {"color" : "salmon" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"xl" , "qty" :58},
                                    {"size":"xxL" , "qty" : 30}]},
        ] },
     {"style": "D", "composition":[ 
        {"color" : "white" , "size": [{"size":"S" , "qty" : 15},
                                    {"size":"M" , "qty" : 18},
                                    {"size":"L" , "qty" : 35},
                                    {"size":"xL" , "qty" : 45},
                                    {"size":"xxL" , "qty" : 55},
                                    ]},
        {"color" : "orange" , "size": [{"size":"S" , "qty" : 15},
                                    {"size":"M" , "qty" : 18},
                                    {"size":"L" , "qty" : 35},
                                    {"size":"xL" , "qty" : 45},
                                    {"size":"xxL" , "qty" : 55},
                                    ]},
        {"color" : "brown" , "size": [{"size":"S" , "qty" : 15},
                                    {"size":"M" , "qty" : 18},
                                    {"size":"L" , "qty" : 35},
                                    {"size":"xL" , "qty" : 45},
                                    {"size":"xxL" , "qty" : 55},
                                    ]},
         {"color" : "lime" , "size": [{"size":"S" , "qty" : 15},
                                    {"size":"M" , "qty" : 18},
                                    {"size":"L" , "qty" : 35},
                                    {"size":"xL" , "qty" : 45},
                                    {"size":"xxL" , "qty" : 55},
                                    ]}
         ]},
      {"style": "E", "composition":
        [ 
        {"color" : "red" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"M" , "qty" : 17},
                                    {"size":"L" , "qty" : 65}]},
        {"color" : "golden" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"M" , "qty" : 17},
                                    {"size":"L" , "qty" : 65}]},
        {"color" : "chocolate" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"M" , "qty" : 17},
                                    {"size":"L" , "qty" : 65}]},
        {"color" : "bronze" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"M" , "qty" : 17},
                                    {"size":"L" , "qty" : 65}]},
         {"color" : "orchid" , "size": [{"size":"S" , "qty" : 20},
                                    {"size":"M" , "qty" : 17},
                                    {"size":"L" , "qty" : 65}]},
        ]
    }]
def getSizeForASpecificColor(orderdata):
  #print(orderdata['size'])
  totalsize = 0
  for thissize in orderdata['size']:
        totalsize += thissize['qty']
        #print( thissize['qty'])
  return totalsize

def getSizeForComposition(orderdata):
  totalsize = 0
  for stylecolor in orderdata:
     colorqty =getSizeForASpecificColor(stylecolor)
     totalsize+=colorqty
     print(stylecolor["color"],colorqty)
  return totalsize
def getSizeforStyle():
    for item in inventory:    
      print(item['style']) 
      print(getSizeForComposition(item['composition'])) 
getSizeforStyle()