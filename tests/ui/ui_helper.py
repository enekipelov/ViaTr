import json
import string
import random

def save_username_to_file(username, path_to_file):
    with open(path_to_file,"r") as jsonFile:
        data = json.load(jsonFile)

    data["username"] = username

    with open(path_to_file, "w") as jsonFile:
        json.dump(data, jsonFile)

def unique_user():
    characters = string.ascii_letters + string.digits
    stamp = ''.join(random.choice(characters) for i in range(8))
    return 'user' + str(stamp)