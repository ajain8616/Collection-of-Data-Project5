current_box = 1
max_capacity = 20
remaining_capacity = max_capacity
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
def openNewBoxIfNeeded():
    global remaining_capacity,current_box,max_capacity
    if remaining_capacity==0:
        remaining_capacity=max_capacity
        current_box=current_box+1
def fillBox(Style,Size,Qty):
    global remaining_capacity,current_box,max_capacity
    while Qty>0:
         if Qty <=remaining_capacity:
             print(f"We are storing {Qty} peices of Size {Size} for Style {Style} in box no.{current_box}")
             print()
             remaining_capacity=remaining_capacity-Qty
             Qty=0
         else:
            print(f"We are storing {remaining_capacity} peices of Size {Size} for Style {Style} in box no.{current_box}") 
            print()
            Qty=Qty-remaining_capacity 
            remaining_capacity=0
         openNewBoxIfNeeded()
for item in inventory:
    for new in item['composition']:
        for newi in new['size']:
            # print('Style:',item['style'],'\nColor:',new['color'],'\nSize:',newi['size'],'\nQTY:',newi['qty'])   
            fillBox(item["style"],newi["size"],newi['qty'])