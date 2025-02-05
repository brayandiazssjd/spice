import json

with open("test/data.json", "r") as file:
    data_list = json.load(file)
print(type(data_list[0]["id"]))
