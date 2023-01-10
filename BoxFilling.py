current_box = 1
max_capacity = 20
remaining_capacity = max_capacity
# print program input
inventory = [
{"style": "A", "qty": 50}, 
{"style": "B", "qty": 24},
{"style": "C", "qty": 45},
{"style": "D", "qty": 35},
{"style": "E", "qty": 45}
]
def openNewBoxIfNeeded():
    global remaining_capacity,current_box,max_capacity
    if remaining_capacity==0:
        remaining_capacity=max_capacity
        current_box=current_box+1
def fillBox(Style,Qty):
    global remaining_capacity,current_box,max_capacity
    while Qty>0:
         if Qty <=remaining_capacity:
             print(f"We are storing {Qty} peices of {Style} in box no.{current_box}")
             remaining_capacity=remaining_capacity-Qty
             Qty=0
         else:
            print(f"We are storing {remaining_capacity} peices of {Style} in box no.{current_box}") 
            Qty=Qty-remaining_capacity 
            remaining_capacity=0
         openNewBoxIfNeeded()
           
for item in inventory:
    print('Style',item['style'], '\nItems:',item['qty'])
    fillBox(item["style"],item["qty"])
