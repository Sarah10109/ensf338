import timeit


before = """
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

"""
testcode = """

change(largeFile)
"""

time = timeit.timeit(stmt=testcode,setup=before, number=10)

average = time/10
print(average)



