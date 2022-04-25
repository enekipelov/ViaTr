import json
import os
from pathlib import Path

def save_username_to_file(username):
    p = 'E:/dd/ViaTr/tests/user.json'
    with open(p,"r") as jsonFile:
        data = json.load(jsonFile)

    data["username"] = username

    with open("user.json", "w") as jsonFile:
        json.dump(data, jsonFile)