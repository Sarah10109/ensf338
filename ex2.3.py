import json
import pandas as pd    

largeFile = open("large-file.json", encoding="utf8").read()
largeFile = json.loads(largeFile) 

def update_size(json_obj, new_value):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == 'size':
                json_obj[key] = new_value
            elif isinstance(value, (dict, list)):
                update_size(value, new_value)
    elif isinstance(json_obj, list):
        for item in json_obj:
            update_size(item, new_value)

# Example usage:

update_size(largeFile, 35)

reverse = list(reversed(largeFile))

with open('output.2.3.json', 'w') as f:
    json.dump(reverse, f, indent= 4)


