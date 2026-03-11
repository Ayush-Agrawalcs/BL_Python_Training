import json
data = {"name": "Ayush", "age": 22, "city": "Delhi"}
parse=json.dumps(data)
print(type(parse))