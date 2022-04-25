import os
import json
def get_username_from_file():
    p = 'E:/dd/ViaTr/tests/user.json'
    with open(p,"r") as jsonFile:
        data = json.load(jsonFile)

    return data["username"]
print(get_username_from_file())