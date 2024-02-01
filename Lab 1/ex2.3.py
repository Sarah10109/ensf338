import json

largeFile = open("large-file.json", encoding="utf8").read()
largeFile = json.loads(largeFile) 

def change(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'size':
                obj[key] = 35
            elif isinstance(value, (dict, list)):
                change(value)
    elif isinstance(obj, list):
        for item in obj:
            change(item)

change(largeFile)

reverse = list(reversed(largeFile))

with open('output.2.3.json', 'w') as f:
    json.dump(reverse, f, indent= 4)


