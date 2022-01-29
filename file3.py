import json
f1 = open("States.json","r")
data  = json.load(f1)
#print(data)
#for s in data:
 #   print(s)
for s in data['states']:
     #print(s)
    #print(s['name'], s['abbreviation'])
    #if len(s['area_codes']) > 2:
     #   print(s['name'])
    print(s['name'],len(s['area_codes']))